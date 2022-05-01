#!/bin/sh

pages=$(cd "$(dirname "$0")/../_pages" && pwd)
errors=0

# Check that user page name matches GitHub ID.

for f in "$pages/people/"*
do
  user=${f##*/}
  user=${user%.md}
  github=$(grep -o "github: .*" "$f")
  github=${github#github: }
  test "$github" -a "$github" != "$user" && {
    echo "$user: GitHub ID mismatch: $github"
    errors=$((errors+1))
  }
done

# Check that person include id references exist.

ids1=$(grep -IRo '{% include person id=[^%]*%}' "$pages" | sed 's/.* id=.//' | sed "s/['\"].*//")
ids2=$(grep -IRo '{% include person-list ids=[^%]*%}' "$pages" | sed 's/.* ids=.//' | sed "s/['\"].*//" | tr '|' '\n')
ids=$(echo "$ids1" "$ids2" | sort -u | grep -v ' ')
for id in $ids
do
  test -f "$pages/people/$id.md" || {
    echo "Unknown person ID: $id"
    errors=$((errors+1))
  }
done
test "$errors" -gt 255 && errors=255
exit $errors
