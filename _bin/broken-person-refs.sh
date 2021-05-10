#!/bin/sh

pages=$(cd "$(dirname "$0")/../_pages" && pwd)

ids1=$(grep -IRo '{% include person id=[^%]*%}' "$pages" | sed 's/.* id=.//' | sed "s/['\"].*//")
ids2=$(grep -IRo '{% include person-list ids=[^%]*%}' "$pages" | sed 's/.* ids=.//' | sed "s/['\"].*//" | tr '|' '\n')
echo "$ids1" "$ids2" | sort -u | while read id
do
  echo "$id" | grep -q ' ' && continue # not a person ID
  test -f "$pages/users/$id.md" || echo "$id"
done
