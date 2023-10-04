#!/usr/bin/env bash
# a script that make directory and Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update
    apt-get install -y nginx
fi

folders=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
    fi
done

fake_html="/data/web_static/releases/test/index.html"
echo "Fake Content" > "$fake_html"

symlink="/data/web_static/current"
if [ -L "$symlink" ]; then
    rm "$symlink"
fi
ln -s /data/web_static/releases/test/ "$symlink"

chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sed -i '/^[\s]*location \/ {$/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"

service nginx restart
