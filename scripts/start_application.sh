#!/bin/bash
cd /home/ec2-user/www/fastube/
source /home/ec2-user/www/fastube-venv/bin/activate
python /home/ec2-user/www/fastube/fastube/manage.py collectstatic
