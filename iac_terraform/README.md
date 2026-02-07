# Terraform Installation Playbook

This README explains the Ansible playbook for installing HashiCorp Terraform on Debian systems. The playbook handles GPG key management, repository configuration, and package installation with dynamic architecture detection.

## Playbook Overview

**File:** `terra.yml`

**Purpose:** Install HashiCorp Terraform on localhost with proper GPG signature verification

**Execution:** 
```bash
ansible-playbook terraform/terra.yml
```

## Playbook Plays/Tasks

### 1. Install Required Packages

```yaml
- name: Install required packages
  ansible.builtin.apt:
    name: gnupg
    state: present
```

**Purpose:** Installs `gnupg` (GNU Privacy Guard), which is required to handle GPG key operations.

**Why It's Needed:** The playbook downloads a GPG key and converts it from ASCII armor format (`--dearmor`), which requires the `gpg` command-line tool.

**Example Output:**
```
TASK [Install required packages] ***
ok: [localhost]
```

**Lesson Learned:** Always install dependencies upfront. The `apt-key` module is deprecated in newer Debian versions and will fail with "Failed to find required executable 'apt-key'" error.

---

### 2. Get Distribution Codename

```yaml
- name: Get distribution codename
  ansible.builtin.shell: lsb_release -cs
  register: distro_codename
  changed_when: false
```

**Purpose:** Retrieves the distribution codename (e.g., "trixie", "bookworm") and stores it in a variable.

**Key Concepts:**
- `ansible.builtin.shell`: Executes shell commands
- `register`: Captures output in a variable (`distro_codename`)
- `changed_when: false`: Marks this as informational, not a system change

**Example Output:**
```
TASK [Get distribution codename] ***
ok: [localhost]

# The variable distro_codename.stdout contains: "trixie"
```

**Lesson Learned:** Shell variables like `$(lsb_release -cs)` don't work in Ansible modules. You must capture them as task variables first.

---

### 3. Get System Architecture

```yaml
- name: Get system architecture
  ansible.builtin.shell: dpkg --print-architecture
  register: system_arch
  changed_when: false
```

**Purpose:** Detects the system architecture (e.g., "amd64", "arm64") for package compatibility.

**Key Concepts:**
- Stores architecture in `system_arch.stdout`
- Required for dynamic repository URL construction

**Example Outputs:**
```bash
# On amd64 systems:
amd64

# On arm64 systems (like this dev container):
arm64
```

**Lesson Learned:** Hardcoding `arch=amd64` fails on arm64 systems with "No package matching 'terraform' is available". Always detect the architecture dynamically.

---

### 4. Download and Add Hashicorp GPG Key

```yaml
- name: Download and add Hashicorp GPG key
  ansible.builtin.shell: |
    curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor > /usr/share/keyrings/hashicorp-archive-keyring.gpg
  changed_when: false
```

**Purpose:** Downloads HashiCorp's GPG public key and converts it from ASCII armor format to binary format for use by apt.

**Command Breakdown:**
- `curl -fsSL`: Downloads the GPG key silently
  - `-f`: Fail silently on server errors
  - `-s`: Silent mode
  - `-S`: Show errors even in silent mode
  - `-L`: Follow redirects
- `gpg --dearmor`: Converts ASCII-armored key to binary format
- Output saved to `/usr/share/keyrings/hashicorp-archive-keyring.gpg`

**Example Output:**
```
TASK [Download and add Hashicorp GPG key] ***
ok: [localhost]
```

**Lesson Learned:** Modern apt (Debian 12+) requires signed repositories. Use `signed-by=/path/to/keyring.gpg` in the repository URL instead of the deprecated `apt-key` command.

---

### 5. Add Hashicorp Repository

```yaml
- name: Add hashicorp repository
  ansible.builtin.apt_repository:
    repo: "deb [arch={{ system_arch.stdout | trim }} signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com {{ distro_codename.stdout | trim }} main"
    state: present
    filename: hashicorp
```

**Purpose:** Adds the HashiCorp official APT repository with GPG signature verification.

**Key Components:**
- `[arch={{ system_arch.stdout | trim }}]`: Specifies architecture (dynamically detected)
- `signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg`: Points to GPG keyring for verification
- `https://apt.releases.hashicorp.com`: Official HashiCorp repository URL
- `{{ distro_codename.stdout | trim }}`: Debian codename directory (e.g., trixie)
- `| trim`: Removes whitespace (prevents malformed URLs)

**Example Repository URL Generated:**
```
deb [arch=arm64 signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com trixie main
```

**Lesson Learned:** 
- Shell variable substitution `$(lsb_release -cs)` doesn't work in module parameters—use Jinja2 templating with registered variables
- Always use the `| trim` filter when inserting shell output into URLs to remove trailing newlines
- Without the `| trim` filter, you get errors: "does not have a Release file"

---

### 6. Update APT Cache

```yaml
- name: Update apt cache
  ansible.builtin.apt:
    update_cache: yes
```

**Purpose:** Refreshes the apt package cache after adding the new repository.

**Why It's Needed:** Apt needs to fetch the package lists from the newly added repository before installation.

**Example Output:**
```
TASK [Update apt cache] ***
ok: [localhost]
```

---

### 7. Install Hashicorp Terraform

```yaml
- name: Install hashicorp terraform
  ansible.builtin.package:
    name: terraform
    state: present
```

**Purpose:** Installs the terraform package from the configured repository.

**Key Concepts:**
- `ansible.builtin.package`: Abstraction that works across different package managers (apt, yum, etc.)
- `state: present`: Ensures the package is installed

**Example Output:**
```
TASK [Install hashicorp terraform] ***
changed: [localhost] => {"cache_update_time": 1707328947, "cache_updated": true, "installed_packages": ["terraform"]}
```

**Verification After Installation:**
```bash
terraform --version
# Output: Terraform v1.x.x on linux_arm64
```

---

## Common Errors and Solutions

### Error 1: `Failed to find required executable "apt-key"`
**Cause:** Using deprecated `ansible.builtin.apt_key` module on Debian 12+

**Solution:** Use `ansible.builtin.shell` with `gpg --dearmor` and `signed-by=` parameter instead

### Error 2: `No package matching 'terraform' is available`
**Cause:** Hardcoded `arch=amd64` on arm64 system

**Solution:** Dynamically detect architecture with `dpkg --print-architecture` and use in repository URL

### Error 3: `does not have a Release file`
**Cause:** Malformed repository URL with trailing whitespace

**Solution:** Use Jinja2 `| trim` filter: `{{ variable.stdout | trim }}`

### Error 4: `W: OpenPGP signature verification failed`
**Cause:** Invalid or missing GPG key for repository

**Solution:** 
- Ensure GPG key is downloaded correctly
- Verify `signed-by=` path in repository URL matches the keyring location

---

## Key Ansible Concepts Demonstrated

| Concept | Example | Purpose |
|---------|---------|---------|
| `register` | `register: distro_codename` | Capture task output for reuse |
| `changed_when: false` | Information gathering tasks | Mark non-destructive tasks as informational |
| Jinja2 templating | `{{ variable.stdout \| trim }}` | Dynamic variable substitution |
| `\| trim` filter | `{{ output \| trim }}` | Remove whitespace from strings |
| `ansible.builtin.shell` | Execute shell commands | Run custom system commands |
| `ansible.builtin.apt_repository` | Add APT repositories | Manage package sources |
| `ansible.builtin.apt` | Manage packages and cache | Install/remove packages |

---

## References

- [Terraform Official APT Repository Documentation](https://apt.releases.hashicorp.com/)
- [Ansible apt_repository Module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html)
- [Ansible Filters - String Manipulation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html)
- [Debian Package Management](https://wiki.debian.org/SecureApt)
- [GPG Key Management in Debian](https://manpages.debian.org/apt-key)

---

## Testing the Playbook

```bash
# Run the playbook
ansible-playbook terraform/terra.yml

# Verify installation
terraform --version

# Check repository configuration
apt-cache policy terraform

# View repository details
cat /etc/apt/sources.list.d/hashicorp.list
```
