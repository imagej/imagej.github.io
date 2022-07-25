#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

documented=$(grep -A99999 '# Available includes' _pages/editing/index.md |
  grep '^| [a-z\[]' | sed 's/^| \[*\([a-z-]*\).*/\1/')

errors=0

for f in _includes/*
do
  test -d "$f" && continue
  inc=${f#_includes/}
  echo "$documented" | grep -q "^$inc$" || { echo "[ERROR] Undocumented: $inc"; errors=$((errors+1)); }
done

echo "$documented" | while read inc
do
  test -f "_includes/$inc" || { echo "[ERROR] Nonexistent: $inc"; errors=$((errors+1)); }
done

test $errors -gt 255 && errors=255
exit $errors
