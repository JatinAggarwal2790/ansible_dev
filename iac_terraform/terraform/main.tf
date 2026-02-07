terraform {
  required_version = ">= 1.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

# Update APT cache before installing packages
resource "terraform_data" "update_apt" {
  provisioner "local-exec" {
    command = "sudo apt-get update"
  }
}

# Wait for apt lock to be released before chrony installation
resource "terraform_data" "wait_after_update" {
  provisioner "local-exec" {
    command = "sleep 2"
  }

  depends_on = [terraform_data.update_apt]
}

# Install chrony service (time synchronization)
resource "terraform_data" "install_chrony" {
  provisioner "local-exec" {
    command = "for i in {1..5}; do sudo apt-get install -y chrony && break || sleep 2; done"
  }

  depends_on = [terraform_data.wait_after_update]
}

# Start and enable chrony service
resource "terraform_data" "enable_chrony" {
  provisioner "local-exec" {
    command = "sudo systemctl enable chrony && sudo systemctl start chrony || true"
  }

  depends_on = [terraform_data.install_chrony]
}

# Wait before installing httpd
resource "terraform_data" "wait_after_chrony" {
  provisioner "local-exec" {
    command = "sleep 2"
  }

  depends_on = [terraform_data.enable_chrony]
}

# Install httpd (Apache HTTP Server)
resource "terraform_data" "install_httpd" {
  provisioner "local-exec" {
    command = "for i in {1..5}; do sudo apt-get install -y apache2 && break || sleep 2; done"
  }

  depends_on = [terraform_data.wait_after_chrony]
}

# Start and enable Apache service
resource "terraform_data" "enable_httpd" {
  provisioner "local-exec" {
    command = "sudo systemctl enable apache2 && sudo systemctl start apache2 || true"
  }

  depends_on = [terraform_data.install_httpd]
}

# Output installation status
output "installation_status" {
  value = "Chrony and Apache HTTP Server installation completed"
}