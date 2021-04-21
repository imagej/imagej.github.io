#!/bin/sh

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

prefixes="
ij
conference
list-of-update-sites
mbf
presentations
tickets
workshops
"

allowed() {
  for prefix in $prefixes
  do
    echo "$1" | grep -q "^/$prefix" && return 0
  done
  return 1
}

grep -IRo 'href="\/[^"]*' "$root" | sed 's/:href="/:/' | while read line
do
  file=${line%%:*}
  file=${file##*/_site/}
  link=${line#*:}
  page=${link%#*}
  test "$page" = "$link" && anchor="" || anchor=${link#*#}
  target="$root$page"
  test -f "$target" -o -f "$target.html" -o -f "$target/index.html" || allowed "$link" ||
   { echo "$link"; continue; }
  test -z "$anchor" || allowed "$link" ||
    grep -q "id=\"$anchor\"" "$target.html" 2>/dev/null ||
    grep -q "id=\"$anchor\"" "$target/index.html" 2>/dev/null ||
    echo "$link [NO ANCHOR]"
done
