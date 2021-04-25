#!/bin/sh

# Search for a particular query string from the CLI. Useful for testing.

hostname=search.imagej.net
prefix="https://$hostname:8108"
collection=imagej-wiki

TYPESENSE_API_KEY=$(cat /etc/typesense/typesense-server.ini | grep '^api-key = ' | sed 's/^api-key = //')
curl -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" "$prefix/collections/$collection/documents/search?q=$1&query_by=title"
