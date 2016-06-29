#!/usr/bin/env bash
/etc/init.d/nginx stop

chown ec2-user:ec2-user /home/ec2-user/www

mkdir -p /home/ec2-user/www/fastube-venv/
pyenv deactivate
pyenv uninstall -f fastube
pyenv virtualenv 3.5.1 fastube

chown ec2-user:ec2-user /home/ec2-user/www/fastube-venv
chown ec2-user:ec2-user /home/ec2-user/www/fastube-venv/*
pyenv activate fastube

pip3 install -r /home/ec2-user/www/fastube/requirements.txt
