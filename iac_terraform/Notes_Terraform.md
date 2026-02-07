cd /workspaces/Ansible/terraform
terraform init
terraform plan
terraform apply


ansible-galaxy collection install community.general
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/community-general-12.3.0.tar.gz to /home/vscode/.ansible/tmp/ansible-local-27453v9pgd7mm/tmp62a2m5mf/community-general-12.3.0-zmzsp3zy
Installing 'community.general:12.3.0' to '/home/vscode/.ansible/collections/ansible_collections/community/general'
community.general:12.3.0 was installed successfully



(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/iac_terraform (main) $ ansible-playbook manage_terraform.yaml 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Terraform] ************************************************************************************************************************************************************************************************************

TASK [Apply or destroy resources with terraform] ****************************************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP ******************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/iac_terraform (main) $ ansible-playbook manage_terraform.yaml -e terraform_state=absent
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Terraform] ************************************************************************************************************************************************************************************************************

TASK [Apply or destroy resources with terraform] ****************************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP ******************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(ansible-tuts-py3.14) vscode ➜ /workspaces/Ansible/iac_terraform (main) $ ansible-playbook manage_terraform.yaml -e terraform_state=absent