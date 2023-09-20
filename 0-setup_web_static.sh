#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.


sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create the following folders if they don’t already exist:
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file with sample to test Nginx configuration
echo "Hello, this is a test HTML file." | sudo tee /data/web_static/releases/test/index.html

# Remove the symbolic link /data/web_static/current from the web server
sudo rm -rf /data/web_static/current

# Create a symbolic link. If the symbolic link already exists, it is deleted and recreated every time the script is ran.
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static.
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart nginx after updating the configuration.
sudo service nginx restart