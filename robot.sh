#!/usr/bin/env sh
systemctl stop webiopi.service
webiopi -d -c /etc/webiopi/config
