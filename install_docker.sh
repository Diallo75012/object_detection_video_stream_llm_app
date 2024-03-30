#!/bin/bash

# update and upgrade
sudo apt update -y
sudo apt upgrade -y
# update apt packages index and enable ability to use https repos
sudo apt-get install ca-certificates  curl gnupg lsb-release -y
# add docker official GPG keys
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# configure stable repo, add nightly or test after 'stable' in the command if needed to have those ones as well
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# update again
sudo apt update -y
# install docker
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
# enable docker
sudo systemctl start docker
sudo systemctl enable docker
# check status
sudo systemctl status docker
# check versions docker and docker-compose
docker --version
docker compose version
# add user to docker group and restart computer to have those changes make effect
sudo usermod -aG docker $USER
echo "User added to docker group computer will restart for this change to take effect! No Choice Mate!"
sudo reboot
