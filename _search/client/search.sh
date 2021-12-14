#!/bin/sh

# Search for a particular query string from the CLI. Useful for testing.

dir=$(dirname "$(echo "$0")")

hostname=search.imagej.net
prefix="https://$hostname:8108"
collection=imagej-web

TYPESENSE_API_KEY=$(cat "$dir/src/app.js" | grep '^ *apiKey: ' | sed 's/.*apiKey: "\([^"]*\)".*/\1/')

which json_pp >/dev/null 2>&1 && pretty=json_pp || pretty=cat

curl -fs -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" "$prefix/collections/$collection/documents/search?q=$1&query_by=title" | $pretty
