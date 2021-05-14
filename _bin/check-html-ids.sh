#!/bin/bash

# Scans HTML element id values for duplicates.

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

errors=0
while read f
do
  sf=$(echo "$f" | sed "s:^$root::")
  output=$(grep -oh ' id="[^"]*"' "$f" | sort | uniq -d | sed 's/^/-->/')
  test "$output" && echo "[$sf]" && echo "$output" && errors=$((errors+1))
done <<< "$(find "$root" -name '*.html')"
test $errors -gt 255 && errors=255
exit $errors
