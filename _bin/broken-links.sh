#!/bin/sh

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

grep -IRo 'href="\/[^"]*' "$root" | sed 's/:href="/:/' | while read line
do
  file=${line%%:*}
  file=${file##*/_site/}
  link=${line#*:}
  target="$root$link"
  test -f "$target" -o -f "$target.html" -o -f "$target/index.html" ||
    { echo "$link"; }
done
