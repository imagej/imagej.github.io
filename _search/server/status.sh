#!/bin/sh

# Echoes the status of the running typesense-server.

hostname=search.imagej.net
prefix="https://$hostname:8108"

echo "[Service status]"
systemctl status typesense-server.service

echo
echo "[Server health check]"
curl "$prefix/health"
echo

echo
echo "[Configuration file]"
ls -la /etc/typesense/typesense-server.ini

echo
echo "[Collection statistics]"
TYPESENSE_API_KEY=$(cat /etc/typesense/typesense-server.ini | grep '^api-key = ' | sed 's/^api-key = //')
curl -fs -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" "$prefix/collections" | json_pp
