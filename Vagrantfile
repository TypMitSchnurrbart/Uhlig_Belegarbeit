Vagrant.configure("2") do |config|

  # Install the ubuntu vm
  config.vm.box = "ubuntu/focal64"

  # Get up to date
  config.vm.provision "shell", inline: "apt update"

  # Install ansible
  config.vm.provision "shell", inline: "apt-get install ansible -y"
  config.vm.provision "shell", inline: "apt-get install git -y"

  # Forward HTTP Port
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Load the ansible playbook
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
  end

end
