# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "debian/jessie64"

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--cpuexecutioncap", "10"]
    v.cpus = 1
    v.memory = "150"
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080
  #config.vm.network "public_network"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "app.yml"
    ansible.inventory_path = "hosts"
    ansible.limit= "test"
    ansible.become = true
  end
end
