# steam-organizer - backend
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
1. In the project folder, execute `vagrant up`
1. After VM setup, run `vagrant ssh` to connect to virtual machine
1. Go to vagrant shared folder: `cd /vagrant`

+ To start Gunicorn Server, run the following command: `./start-gunicorn.sh`
+ To start the Celery batch job, execute: `./start-celery.sh`
