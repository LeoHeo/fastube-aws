#!/bin/bash

mkdir -p /etc/nginx/sites-enabled
mkdir -p /etc/nginx/sites-available

sudo mkdir -p /etc/nginx/log/

sudo cp /home/ec2-user/www/fastube/nginx/default.conf /etc/nginx/nginx.conf

sudo unlink /etc/nginx/sites-enbled/*

sudo cp /home/ec2-user/www/fastube/nginx/production.conf /etc/nginx/sites-available/fastube-host.conf

sudo ln -s /etc/nginx/sites-available/fastube-host.conf /etc/nginx/sites-enabled/fastube-host.conf

sudo /etc/init.d/nginx reload
sudo /etc/init.d/nginx start
