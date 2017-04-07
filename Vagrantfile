# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

$setupScript = <<SCRIPT
echo provisioning docker...
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
sudo apt-get install python3-pip -y && sudo pip3 install pyyaml
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install -y docker-ce
sudo usermod -a -G docker vagrant

SCRIPT

Vagrant.configure("2") do |config|

  # create node
  config.vm.define :vagrant do |config|
      config.vm.box = "bento/ubuntu-16.04"
      config.vm.hostname = "vagrant"
      config.vm.network :private_network, ip: "10.1.15.10"
      config.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = "1"
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      end
      config.vm.provision :shell, :inline => $setupScript
  end

end
