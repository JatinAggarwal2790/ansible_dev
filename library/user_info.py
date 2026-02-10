#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import pwd

def run_module():
    # define available arguments/parameters a user can pass to the module
    # module_args = dict(
    #     username=dict(type='str', required=True),
    #     new=dict(type='bool', required=False, default=False)
    # )
    module_args = {
        'username': dict(type='str', required=True),
        
    }
    # result = dict(
    #     changed=False,
    #     original_message='',
    #     message=''
    # )
    result = {
        'changed': False,
        'failed': True,
        'message': 'Failed to fetch user information'
    }
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    try:
        user_info = pwd.getpwnam(module.params['username'])

    except KeyError:
        result['message'] = 'User not found'
        module.exit_json(**result)
    
    # result['changed'] = False
    result['failed'] = False
    result['message'] = 'User information fetched successfully'
    result['user_info'] = {
        'username': user_info.pw_name,
        'uid': user_info.pw_uid,
        'gid': user_info.pw_gid,
        'home': user_info.pw_dir,
        'shell': user_info.pw_shell
    }
    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()