#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Pytroll developers
#
# Author(s):
#
#   Martin Raspaud <martin.raspaud@smhi.se>
#   Panu Lahtinen <pnuu+git@iki.fi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from logging import getLogger
try:
    from posttroll.listener import ListenerContainer
except ImportError:
    ListenerContainer = None
from six.moves.queue import Empty as queue_empty

import yaml
try:
    from yaml import UnsafeLoader, BaseLoader
except ImportError:
    from yaml import Loader as UnsafeLoader
    from yaml import BaseLoader

from trollflow2.dict_tools import gen_dict_extract, plist_iter
from trollflow2.plugins import AbortProcessing
from collections import OrderedDict
import copy
from six.moves.urllib.parse import urlparse
import traceback
import gc

"""The order of basic things is:
- Create the scene
- Generate the composites
- Resample
- Save to file
"""

LOG = getLogger("launcher")
DEFAULT_PRIORITY = 999


def get_test_message(test_message_file):
    """Read file and retrieve the test message"""

    msg = None
    if test_message_file:
        with open(test_message_file) as fpt:
            msg = fpt.readline().strip('\n')

    return msg


def run(prod_list, topics=None, test_message=None):

    tmessage = get_test_message(test_message)
    if tmessage:
        from threading import Thread as Process
        from posttroll.message import Message
    else:
        from multiprocessing import Process

    with open(prod_list) as fid:
        config = yaml.load(fid.read(), Loader=BaseLoader)
    topics = topics or config['product_list'].pop('subscribe_topics', None)

    if not tmessage:
        listener = ListenerContainer(topics=topics)

    while True:
        try:
            if tmessage:
                msg = Message(rawstr=tmessage)
            else:
                msg = listener.output_queue.get(True, 5)
        except KeyboardInterrupt:
            if not tmessage:
                listener.stop()
            return
        except queue_empty:
            continue

        proc = Process(target=process, args=(msg, prod_list))
        proc.start()
        proc.join()
        if tmessage:
            break


def get_area_priorities(product_list):
    """Get processing priorities and names for areas."""
    priorities = {}
    plist = product_list['product_list']['areas']
    for area in plist.keys():
        prio = plist[area].get('priority', DEFAULT_PRIORITY)
        if prio is None:
            prio = DEFAULT_PRIORITY
        if prio not in priorities:
            priorities[prio] = [area]
        else:
            priorities[prio].append(area)

    return priorities


def message_to_jobs(msg, product_list):
    """Convert a posttroll message *msg* to a list of jobs given a *product_list*."""
    formats = product_list['product_list'].get('formats', None)
    for _product, pconfig in plist_iter(product_list['product_list'], level='product'):
        if 'formats' not in pconfig and formats is not None:
            pconfig['formats'] = formats.copy()
    jobs = OrderedDict()
    priorities = get_area_priorities(product_list)
    # TODO: check the uri is accessible from the current host.
    input_filenames = [urlparse(uri).path for uri in gen_dict_extract(msg.data, 'uri')]
    for prio, areas in priorities.items():
        jobs[prio] = OrderedDict()
        jobs[prio]['input_filenames'] = input_filenames.copy()
        jobs[prio]['input_mda'] = msg.data.copy()
        jobs[prio]['product_list'] = {}
        for section in product_list:
            if section == 'product_list':
                if section not in jobs[prio]['product_list']:
                    jobs[prio]['product_list'][section] = OrderedDict(product_list[section].copy())
                    del jobs[prio]['product_list'][section]['areas']
                    jobs[prio]['product_list'][section]['areas'] = OrderedDict()
                for area in areas:
                    jobs[prio]['product_list'][section]['areas'][area] = product_list[section]['areas'][area]
            else:
                jobs[prio]['product_list'][section] = product_list[section]

    return jobs


def expand(yml):
    """Expand a yaml config so that aliases are copied.

    PFE http://disq.us/p/1tdbxgx
    """
    if isinstance(yml, dict):
        for key, value in yml.items():
            if isinstance(value, dict):
                expand(value)
                yml[key] = copy.deepcopy(yml[key])
    return yml


def process(msg, prod_list):
    """Process a message."""
    try:
        with open(prod_list) as fid:
            config = yaml.load(fid.read(), Loader=UnsafeLoader)
        config = expand(config)
        jobs = message_to_jobs(msg, config)
        for prio in sorted(jobs.keys()):
            job = jobs[prio]
            job['processing_priority'] = prio
            try:
                for wrk in config['workers']:
                    cwrk = wrk.copy()
                    cwrk.pop('fun')(job, **cwrk)
            except AbortProcessing as err:
                LOG.info(str(err))
    except (IOError, yaml.YAMLError):
        # Either open() or yaml.load() failed
        LOG.exception("Process crashed, check YAML file.")
        return
    except Exception:
        LOG.exception("Process crashed")
        if "crash_handlers" in config:
            trace = traceback.format_exc()
            for hand in config['crash_handlers']['handlers']:
                hand['fun'](config['crash_handlers']['config'], trace)

    # Remove config and run garbage collection so all remaining
    # references e.g. to FilePublisher should be removed
    del config
    gc.collect()


def sendmail(config, trace):
    """Send email about crashes using `sendmail`."""
    from email.mime.text import MIMEText
    from subprocess import Popen, PIPE

    email_settings = config['sendmail']
    msg = MIMEText(email_settings["header"] + "\n\n" + "\n\n" + trace)
    msg["From"] = email_settings["from"]
    msg["To"] = email_settings["to"]
    msg["Subject"] = email_settings["subject"]
    sendmail = email_settings.get("sendmail", "/usr/bin/sendmail")

    pid = Popen([sendmail, "-t", "-oi"], stdin=PIPE)
    pid.communicate(msg.as_bytes())
    pid.terminate()
