# steam-organizer - backend [![Build Status](https://travis-ci.org/rodrigo-kayala/steam-organizer-back.svg)](https://travis-ci.org/rodrigo-kayala/steam-organizer-back)
Steam Organizer is a simple web application to organize, sort and filter your **Steam** game library.

It has been developed as a demonstration purpose of my skills in backend development.

## Main technologies
For backend development the following tools, languagues and technologies has been used:
+ Python 3.4.3
    + Flask 0.10.1
    + flask-mongoengine 0.7.1
    + Flask-OpenID 1.2.4
    + mongoengine 0.10.0
    + pyredis 2.10.3
    + celery 3.1.18
    + gunicorn 19.3.0
+ MongoDB 3.0.6
+ Redis 3.0.3

## How to setup

### Using Vagrant VM

1. Install VirtualBox to be used as a provider: https://www.virtualbox.org/
1. Install Vagrant: https://www.vagrantup.com/
1. Copy vagrant/vagrant_envs_template.sh to vagrant/vagrant_envs.sh (this file
  was intentionaly added to *.gitignore* file)
(e.g. `cp vagrant/vagrant_envs_template.sh  vagrant/vagrant_envs.sh`)
1. Edit your vagrant_envs.sh file and setup the environment variables
  1. You will gonna need a Steam Account to get a Steam Api Key
1. In the project folder, execute `vagrant up`
1. After VM setup, run `vagrant ssh` to connect to virtual machine
1. Go to vagrant shared folder: `cd /vagrant`

+ To start gunicorn server, run the following command: `./start-gunicorn.sh`
+ To start the Celery worker, execute: `./start-celery.sh`
