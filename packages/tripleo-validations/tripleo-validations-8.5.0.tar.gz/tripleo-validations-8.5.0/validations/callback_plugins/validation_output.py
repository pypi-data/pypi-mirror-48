#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import pprint

from ansible.plugins.callback import CallbackBase


FAILURE_TEMPLATE = """\
Task '{}' failed:
Host: {}
Message: {}
"""


WARNING_TEMPLATE = """\
Task '{}' succeeded, but had some warnings:
Host: {}
Warnings:
"""

DEBUG_TEMPLATE = """\
Task: Debug
Host: {}
{}
"""


def indent(text):
    '''Indent the given text by four spaces.'''
    return ''.join('    {}\n'.format(line) for line in text.splitlines())


def print_failure_message(host_name, task_name, results, abridged_result):
    '''Print a human-readable error info from Ansible result dictionary.'''
    def is_script(results):
        return ('rc' in results and
                'invocation' in results and
                results['invocation'].get('module_name') == 'script' and
                '_raw_params' in results['invocation'].get('module_args', {}))

    display_full_results = False
    if 'rc' in results and 'cmd' in results:
        command = results['cmd']
        # The command can be either a list or a string. Concat if it's a list:
        if type(command) == list:
            command = " ".join(results['cmd'])
        message = "Command `{}` exited with code: {}".format(
            command, results['rc'])
        # There may be an optional message attached to the command. Display it:
        if 'msg' in results:
            message = message + ": " + results['msg']
    elif is_script(results):
        script_name = results['invocation']['module_args']['_raw_params']
        message = "Script `{}` exited with code: {}".format(
            script_name, results['rc'])
    elif 'msg' in results:
        message = results['msg']
    else:
        message = "Unknown error"
        display_full_results = True
    print(FAILURE_TEMPLATE.format(task_name, host_name, message))
    stdout = results.get('module_stdout', results.get('stdout', ''))
    if stdout:
        print('stdout:')
        print(indent(stdout))
    stderr = results.get('module_stderr', results.get('stderr', ''))
    if stderr:
        print('stderr:')
        print(indent(stderr))
    if display_full_results:
        print("Could not get an error message. Here is the Ansible output:")
        pprint.pprint(abridged_result, indent=4)
    warnings = results.get('warnings', [])
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print("*", warning)
        print("")


# TODO(shadower): test with async settings
class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'validation_output'

    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display)

    def v2_playbook_on_play_start(self, play):
        pass  # No need to notify that a play started

    def v2_playbook_on_task_start(self, task, is_conditional):
        pass  # No need to notify that a task started

    def v2_runner_on_ok(self, result, **kwargs):
        host_name = result._host
        task_name = result._task.get_name()
        results = result._result  # A dict of the module name etc.
        self._dump_results(results)
        warnings = results.get('warnings', [])
        # Print only tasks that produced some warnings:
        if warnings:
            print(WARNING_TEMPLATE.format(task_name, host_name))
            for warning in warnings:
                print("*", warning)

        # Print the result of debug module
        if (('invocation' in results) and
           ('module_name' in results['invocation'])):

            if ((results['invocation']['module_name'] == 'debug') and
               ('module_args' in results['invocation'])):

                output = ""

                # Variable and its value
                if 'var' in results['invocation']['module_args']:
                    variable = results['invocation']['module_args']['var']
                    value = results[variable]
                    output = "{}: {}".format(variable, str(value))

                # Debug message
                elif 'msg' in results['invocation']['module_args']:
                    output = "Message: {}".format(
                             results['invocation']['module_args']['msg'])

                print(DEBUG_TEMPLATE.format(host_name, output))

    def v2_runner_on_failed(self, result, **kwargs):
        host_name = result._host
        task_name = result._task.get_name()

        result_dict = result._result  # A dict of the module name etc.
        abridged_result = self._dump_results(result_dict)

        if 'results' in result_dict:
            # The task is a list of items under `results`
            for item in result_dict['results']:
                if item.get('failed', False):
                    print_failure_message(host_name, task_name, item, item)
        else:
            # The task is a "normal" module invocation
            print_failure_message(host_name, task_name, result_dict,
                                  abridged_result)

    def v2_runner_on_skipped(self, result, **kwargs):
        pass  # No need to print skipped tasks

    def v2_runner_on_unreachable(self, result, **kwargs):
        host_name = result._host
        task_name = result._task.get_name()
        results = {'msg': 'The host is unreachable.'}
        print_failure_message(host_name, task_name, results, results)

    def v2_playbook_on_stats(self, stats):
        def failed(host):
            return (stats.summarize(host).get('failures', 0) > 0 or
                    stats.summarize(host).get('unreachable', 0) > 0)

        hosts = sorted(stats.processed.keys())
        failed_hosts = [host for host in hosts if failed(host)]

        if hosts:
            if failed_hosts:
                if len(failed_hosts) == len(hosts):
                    print("Failure! The validation failed for all hosts:")
                    for failed_host in failed_hosts:
                        print("*", failed_host)
                else:
                    print("Failure! The validation failed for hosts:")
                    for failed_host in failed_hosts:
                        print("*", failed_host)
                    print("and passed for hosts:")
                    for host in [h for h in hosts if h not in failed_hosts]:
                        print("*", host)
            else:
                print("Success! The validation passed for all hosts:")
                for host in hosts:
                    print("*", host)
        else:
            print("Warning! The validation did not run on any host.")
