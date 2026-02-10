from ansible.errors import AnsibleFilterError
class FilterModule:
    def filters(self):
        return {
            "upper_case": self.to_upper,
        }
    def to_upper(self, value):
        if not isinstance(value, str):
            raise AnsibleFilterError("upper_case expects a string")
        return value.upper()
