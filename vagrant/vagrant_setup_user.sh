#!/bin/bash
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv --python=/usr/bin/python3 python3-app
workon python3-app

echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
echo "workon python3-app" >> ~/.bashrc

pip install -r /vagrant/requirements.txt
