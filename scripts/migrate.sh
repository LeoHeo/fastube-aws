#!/bin/bash
cd /home/ec2-user/www/fastube/

export DJANGO_SETTINGS_MODULE="fastube.settings.production"
export SECRET_KEY="111"

make migrate
