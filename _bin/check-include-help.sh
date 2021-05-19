#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

documented=$(grep -A9999 '# Available includes' _pages/help/editing/index.md |
  grep '^| \[' | sed 's/^| \[\([^]]*\)\].*/\1/')

for f in _includes/*
do
  test -d "$f" && continue
  inc=${f#_includes/}
  echo "$documented" | grep -q "^$inc$" || echo "[ERROR] Undocumented: $inc"
done

echo "$documented" | while read inc
do
  test -f "_includes/$inc" || echo "[ERROR] Nonexistent: $inc"
done
