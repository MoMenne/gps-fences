#!/bin/sh

apt-get update
sudo apt-get install -y python-pip python-dev vim-gui-common

pip install -r requirements.txt
