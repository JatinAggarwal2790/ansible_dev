ansible -m my_test -a 'name=hello new=true' localhost
[WARNING]: No inventory was parsed, only implicit localhost is available
[ERROR]: Task failed: Cannot resolve 'my_test' to an action or module.

Task failed.
Origin: <adhoc 'my_test' task>

{'action': 'my_test', 'args': {'name': 'hello', 'new': 'true'}, 'timeout': 0, 'async_val': 0, 'poll': 15}

<<< caused by >>>

Cannot resolve 'my_test' to an action or module.
Origin: <CLI option '-m'>

my_test

localhost | FAILED! => {
    "changed": false,
    "msg": "Task failed: Cannot resolve 'my_test' to an action or module."
}
(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible (main) $ ANSIBLE_LIBRARY=./library ansible -m my_test -a 'name=hello new=true' localhost
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {
    "changed": true,
    "message": "goodbye",
    "original_message": "hello"