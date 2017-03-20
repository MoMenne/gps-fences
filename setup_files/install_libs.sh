#!/bin/sh

apt-get update
sudo apt-get install -y python-pip python-dev

pip install -r requirements.txt
