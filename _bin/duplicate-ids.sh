#!/bin/sh

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

grep -IRo ' id="[^"]*"' "$root" | sort | uniq -d
