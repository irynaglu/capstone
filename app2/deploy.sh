#!/bin/bash
set -e

echo "Starting deployment..."

# Example: Install necessary packages
yum install -y python3

# Example: Copy application files
cp -r /home/ec2-user/app2/app/* /var/www/html/

# Example: Set up and start the application
python3 /var/www/html/app_code.py &

echo "Deployment completed."