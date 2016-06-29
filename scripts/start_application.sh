#!/usr/bin/env bash

python /home/ec2-user/www/fastube/fastube/manage.py collectstatic
supervisord -c /home/ec2-user/www/fastube/supervisor/default.conf
