#!/bin/sh -e

# /etc/booted/startgpsd.sh

#Need to wait past boot so everything is done
date "+%Y-%m-%d %H:%M:%S" > /startgpsd.txt
sleep 2
echo "Starting GPSD" >> /startgpsd.txt
/usr/sbin/gpsd /dev/ttyUSB0 -G -n -F /var/run/gpsd.sock
date "+%Y-%m-%d %H:%M:%S" >> /startgpsd.txt
exit 0
p
