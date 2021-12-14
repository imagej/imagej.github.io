#!/bin/sh

# Installs typesense-server from the Debian package.
# Use status.sh after installing to check that all is well.

error() { >&2 echo '[ERROR]' $@; }
die() { error $@; exit 1; }
ensureUser() { test "$(whoami)" = "$1" || die "Please run as $1."; }

ensureUser root

hostname=search.imagej.net
collection=imagej-web

# Install the typesense-server Debian package.
wget https://dl.typesense.org/releases/0.19.0/typesense-server-0.19.0-amd64.deb &&
apt install ./typesense-server-0.19.0-amd64.deb &&
rm typesense-server-0.19.0-amd64.deb

# Enable CORS, so that the clients at other addresses can talk to the server.
TYPESENSE_CONFIG_FILE=/etc/typesense/typesense-server.ini
echo 'enable-cors = true' >> "$typesense_config_file" &&
echo "ssl-certificate = /etc/letsencrypt/live/$hostname/fullchain.pem" >> "$TYPESENSE_CONFIG_FILE" &&
echo "ssl-certificate-key = /etc/letsencrypt/live/$hostname/privkey.pem" >> "$TYPESENSE_CONFIG_FILE"

# Create a search-only API key for the appropriate collection.
TYPESENSE_API_KEY=$(cat /etc/typesense/typesense-server.ini | grep '^api-key = ' | sed 's/^api-key = //')
curl "https://$hostname:8108/keys" -X POST -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d "{\"description\":\"Search-only $collection key.\",\"actions\": [\"documents:search\"], \"collections\": [\"$collection\"]}" &&
echo "^^^ Record the above API search key! It cannot be retrieved later. ^^^"
