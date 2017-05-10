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
sudo apt-get -o Dpkg::Options::="--force-confnew" install --force-yes -y docker-ce="17.03.1~ce-0~ubuntu-xenial"
sudo usermod -a -G docker vagrant
curl -L "https://github.com/docker/compose/releases/download/1.13.0/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

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
