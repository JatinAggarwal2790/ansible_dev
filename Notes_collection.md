(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy role init base
- Role base was created successfully
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ cd role
bash: cd: role: No such file or directory
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy role list
# /workspaces/Ansible/roles
- base, (unknown version)
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-playbook testrole.yml 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [test my new module] ********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [base : Run the new module] *************************************************************************************************************************************************************************************************************
changed: [localhost]

TASK [base : Dump test output] ***************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": true,
        "failed": false,
        "message": "This is my test module",
        "original_message": "hello"
    }
}

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-playbook testrole.yml 
[ERROR]: the playbook: testrole.yml could not be found
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-playbook playbooks/testrole.yml 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'
[ERROR]: couldn't resolve module/action 'my_test'. This often indicates a misspelling, missing collection, or incorrect module path.
Origin: /workspaces/Ansible/roles/base/tasks/main.yml:2:3

1 ---
2 - name: Run the new module
    ^ column 3

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-playbook testrole.yml 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [test my new module] ********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [base : Run the new module] *************************************************************************************************************************************************************************************************************
changed: [localhost]

TASK [base : Dump test output] ***************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": true,
        "failed": false,
        "message": "This is my test module",
        "original_message": "hello"
    }
}

TASK [base : Run the User info module] *******************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [base : Dump User output] ***************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": {
        "changed": false,
        "failed": false,
        "message": "User information fetched successfully",
        "user_info": {
            "gid": 1000,
            "home": "/home/vscode",
            "shell": "/bin/bash",
            "uid": 1000,
            "username": "vscode"
        }
    }
}

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
localhost                  : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ mkdir -p collections/ansible_collections
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy collection list
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ cd collections/ansible_collections/
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections/ansible_collections (main) $ ansible-galaxy collection init mac.test
- Collection mac.test was created successfully
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections/ansible_collections (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections/ansible_collections (main) $ cd ..
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ cd..
bash: cd..: command not found
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ cd ..
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy collection list

# /workspaces/Ansible/collections/ansible_collections
Collection Version
---------- -------
mac.test   1.0.0  

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections/ansible_collections (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections/ansible_collections (main) $ cd ..
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ cd..
bash: cd..: command not found
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/collections (main) $ cd ..
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-galaxy collection list

# /workspaces/Ansible/collections/ansible_collections
Collection Version
---------- -------
mac.test   1.0.0  
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ansible-playbook playbooks/test_filter.yml 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test Custom Filter] ********************************************************************************************************************************************************************************************************************

TASK [Test the Filter] ***********************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "HELLO"
}

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ cd collections/ansible_collections/mac/test/
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ansible-galaxy collection build
Created collection for mac.test at /workspaces/Ansible/collections/ansible_collections/mac/test/mac-test-1.0.0.tar.gz
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ls -al
total 12
drwxr-xr-x 9 vscode vscode  288 Feb 10 01:33 .
drwxr-xr-x 3 vscode vscode   96 Feb 10 01:23 ..
drwxr-xr-x 2 vscode vscode   64 Feb 10 01:23 docs
-rw-r--r-- 1 vscode vscode 3090 Feb 10 01:23 galaxy.yml
-rw-r--r-- 1 vscode vscode 2364 Feb 10 01:33 mac-test-1.0.0.tar.gz
drwxr-xr-x 3 vscode vscode   96 Feb 10 01:23 meta
drwxr-xr-x 4 vscode vscode  128 Feb 10 01:25 plugins
-rw-r--r-- 1 vscode vscode   67 Feb 10 01:23 README.md
drwxr-xr-x 2 vscode vscode   64 Feb 10 01:23 roles
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ansible-galaxy list collection
usage: ansible-galaxy [-h] [--version] [-v] TYPE ...
ansible-galaxy: error: argument TYPE: invalid choice: 'list' (choose from collection, role)
 
usage: ansible-galaxy [-h] [--version] [-v] TYPE ...

Perform various Role and Collection related operations.

positional arguments:
  TYPE
    collection          Manage an Ansible Galaxy collection.
    role                Manage an Ansible Galaxy role.

options:
  --version             show program's version number, config file location, configured module search path, module location, executable location and exit
  -h, --help            show this help message and exit
  -v, --verbose         Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might
                        require -vvvv. This argument may be specified multiple times.
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ansible-galaxy collection install mac-test-1.0.0.tar.gz
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'mac.test:1.0.0' to '/home/vscode/.ansible/collections/ansible_collections/mac/test'
mac.test:1.0.0 was installed successfully
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ ansible-galaxy collection list

# /home/vscode/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
community.general 12.3.0 
mac.test          1.0.0  
(ansible-tuts-py3.14) vscode ➜ .../collections/ansible_collections/mac/test (main) $ 