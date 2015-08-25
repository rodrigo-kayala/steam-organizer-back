#!/bin/bash

#cleanup unused packages
apt-get -y remove puppet puppet-common chef

# set locale
locale-gen pt_BR.UTF-8

# python setup
apt-get -y install python-pip
pip install virtualenv virtualenvwrapper

# mongodb setup
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list
apt-get update
apt-get -y install mongodb-org

#redis setup
add-apt-repository -y ppa:rwky/redis
apt-get update
apt-get -y install redis-server
