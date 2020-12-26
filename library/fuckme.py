#!/usr/bin/python
from future import (absolute_import, division, print_function)
metaclass = type
from ansible.plugins.action import ActionBase

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = r'''
---
module: fail
short_description: Fail with custom message
description:
- This module fails the progress with a custom message.
- It can be useful for bailing out when a certain condition is met using C(when).
- This module is also supported for Windows targets.
version_added: "0.8"
options:
  msg:
    description:
    - The customized message used for failing execution.
    - If omitted, fail will simply bail out with a generic message.
    type: str
    default: Failed as requested from task
notes:
    - This module is also supported for Windows targets.
seealso:
- module: assert
- module: debug
- module: meta
author:
- Dag Wieers (@dagwieers)
'''

EXAMPLES = r'''
# Example playbook using fail and when together
- fail:
    msg: The system may not be provisioned according to the CMDB status.
  when: cmdb_status != "to-be-staged"'''

class ActionModule(ActionBase):
    ''' Fail with custom message '''

    TRANSFERS_FILES = False
    _VALID_ARGS = frozenset(('msg',))

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = {}
        del tmp  # tmp no longer has any effect

        msg = 'Failed as requested from task'
        if self._task.args and 'msg' in self._task.args:
            msg = self._task.args.get('msg')

        result['failed'] = True
        result['msg'] = msg
        return result
