#!/usr/bin/env bash
# Set up the web servers for web_static deployment.

# Install Nginx if it is not already installed.
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create the required directories.
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared

# Create a test HTML file.
cat > /data/web_static/releases/test/index.html <<'EOF'
<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>
EOF

# Remove the existing symbolic link or file, then recreate it.
rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Configure Nginx to serve web_static at /hbnb_static/.
python3 - <<'PY'
import re

config = "/etc/nginx/sites-available/default"

with open(config, "r", encoding="utf-8") as file:
    content = file.read()

location = """    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

"""

# Remove an existing copy of this location block, if present.
content = re.sub(
    r"^[ \t]*location /hbnb_static/ \{.*?^[ \t]*\}[ \t]*\n?",
    "",
    content,
    flags=re.MULTILINE | re.DOTALL
)

# Add the location block inside the first server block.
match = re.search(r"server\s*\{", content)
if match:
    content = (
        content[:match.end()]
        + "\n"
        + location
        + content[match.end():]
    )

with open(config, "w", encoding="utf-8") as file:
    file.write(content)
PY

# Give ubuntu ownership of everything under /data.
if id ubuntu >/dev/null 2>&1; then
    chown -R ubuntu:ubuntu /data
else
    echo "Warning: ubuntu user does not exist; skipping ownership change."
fi

# Validate the Nginx configuration and restart Nginx.
if nginx -t; then
    service nginx restart || service nginx start
fi

# Always return a successful exit status.
exit 0
