#!/bin/bash
/etc/init.d/nginx stop

chown ec2-user:ec2-user /home/ec2-user/www

virtualenv --python=python3.4 /home/ec2-user/www/fastube-venv

chown ec2-user:ec2-user /home/ec2-user/www/fastube-venv
pyenv activate fastube

source /home/ec2-user/www/fastube-venv/bin/activate

pip install -r /home/ec2-user/www/fastube/requirements.txt
