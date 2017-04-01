#!/bin/sh -e

if [ ! -f /home/pi/.ssh/id_rsa ]; then
  echo "Generating an RSA key"
  su pi -c 'ssh-keygen -b 2048 -t rsa -f /home/pi/.ssh/id_rsa -q -N ""'
fi

