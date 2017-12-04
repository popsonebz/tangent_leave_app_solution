#curl -O https://raw.githubusercontent.com/popsonebz/tangent_leave_app_solution/master/setup.sh
#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo apt install awscli -y 

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins -y

#cat /var/lib/jenkins/secrets/initialAdminPassword

#install docker
sudo apt-get install -y docker.io
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo usermod -aG docker jenkins
sudo service jenkins restart

#install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.7.5/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
