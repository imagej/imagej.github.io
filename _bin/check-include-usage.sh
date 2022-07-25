#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

check_unfinished() {
  grep -q TODO "$1" && echo "$2 [UNFINISHED]" || echo "$2"
}

matches=$(git grep -ohI '{%-\? *include  *[a-z0-9/-]*' | sed 's/.* //' | grep -v '^extensions/' | sort)
used=$(echo "$matches" | grep -v "^$" | uniq)

# Check for usage of includes that don't exist.
output=$(echo "$used" | while read line
do
  inc=${line##* }
  test -f "_includes/$inc" || {
    echo "[ERROR] Non-existent include used: $inc"
  }
done)
test "$output" && echo "$output" && invalid=$(echo "$output" | wc -l)

# Count how many times each include is used.
count=$(echo "$matches" | uniq -c)
output=$(find _includes -type f | while read f
do
  inc=${f#_includes/}
  test "$inc" = "${inc#extensions/}" || continue # Skip extensions.
  s=$(echo "$count" | grep " $inc$")
  test "$s" || s="      0 $inc"
  grep -q TODO "$f" && echo "$s [UNFINISHED]" || echo "$s"
done | sort -nr)
echo "$output"
unused=$(echo "$output" |
  grep -v ' util/index$' | # Allowed, for symmetry with util/rindex.
  grep '^ *0 ' | wc -l)

errors=$((invalid+unused))
test "$errors" -gt 255 && errors=255
exit $errors
