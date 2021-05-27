#!/bin/sh

# Scans for pages missing from the generated site.

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

errors=0

cd "$root/.."
for f in $(find _pages -name '*.md')
do
  f=${f%.md}
  f=${f#_pages/}
  test -e "_site/$f.html" || { echo "[ERROR] $f not generated"; errors=$((errors+1)); }
done

test $errors -gt 255 && errors=255
exit $errors
