#!/bin/bash

cp ~/Caeborg/sys/.bashrc ~/
cp ~/Caeborg/sys/caeborg.service /etc/systemd/system/caeborg.service
echo "$USER ALL=(root) NOPASSWD: /bin/systemctl" > /etc/sudoers.tmp
