#!/bin/bash
cd /home/ec2-user/www/fastube/
source /home/ec2-user/www/fastube-venv/bin/activate

export DJANGO_SETTINGS_MODULE="fastube.settings.production"
export SECRET_KEY="+7@6ijy6k$8h--&!e6990$fx9$t+1=)dt4&)%at8^!!9pee2bw"

python /home/ec2-user/www/fastube/fastube/manage.py collectstatic --no-input
