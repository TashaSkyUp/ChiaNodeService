#!/bin/bash
#environment
sudo apt install python3-pip
sudo apt install virtualenv
sudo apt-get install python3-venv
echo "creating venv" &&
virtualenv --clear venv &&
echo "activating venv" &&
source ./venv/bin/activate &&
echo "install requirements" &&
pip3 install -r requirements.txt &&

#service
sudo cp chianode.service /etc/systemd/system/ &&
systemctl daemon-reload &&
systemctl start chianode &&
systemctl enable chianode