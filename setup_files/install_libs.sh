#!/bin/sh

apt-get update
sudo apt-get install -y python-pip python-dev vim-gui-common autossh telnet libgeos-dev screen

pip install -r requirements.txt
