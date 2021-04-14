#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

check_unfinished() {
  grep -q TODO "$1" && echo "$2 [UNFINISHED]" || echo "$2"
}

matches=$(git grep -ohI '{% *include  *[a-z0-9-]*' | sed 's/.* //' | sort)
used=$(echo "$matches" | uniq)

# Check for usage of includes that don't exist.
echo "$used" | while read line
do
  inc=${line##* }
  test -f "_includes/$inc" || echo "[ERROR] Non-existent include used: $inc"
done

# Count how many times each include is used.
count=$(echo "$matches" | uniq -c)
for f in _includes/*
do
  inc=${f##*/}
  s=$(echo "$count" | grep " $inc$")
  test "$s" || s="      0 $inc"
  grep -q TODO "$f" && echo "$s [UNFINISHED]" || echo "$s"
done | sort -nr
