from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        with open('./ansible.log', 'a') as f:
            f.write(f"Task '{result.task_name}' succeeded on {result._host}\n")

    def v2_runner_on_failed(self, result, **kwargs):
        with open('./ansible.log', 'a') as f:
            f.write(f"Task '{result.task_name}' failed on {result._host}\n")

    def v2_playbook_on_start(self, playbook):
        with open('./ansible.log', 'a') as f:
            f.write(f"Playbook '{playbook._file_name}' starting...\n")

    def v2_playbook_on_stats(self, stats):
        with open('./ansible.log', 'a') as f:
            f.write(f"Playbook run completed.\n")