#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

output=$(bundle exec htmlproofer $1 \
  --allow-hash-href \
  --assume-extension \
  --check-html \
  --check-img-http \
  --check-opengraph \
  --empty-alt-ignore \
  --report-invalid-tags \
  --report-missing-names \
  --report-script-embeds \
  --report-missing-doctype \
  --report-eof-tags \
  --report-mismatched-tags \
  --url-ignore '/\/(ij|conference|list-of-update-sites|mbf|presentations|tickets|workshops|images|list-of-update-sites)($|\/.*)/' \
  --root-dir="$root" 2>&1)
status=$?
echo "$output" |
  sed 's/ *\* *\([0-9][0-9]*:[0-9][0-9]*\):* *\(.*\)/  *  \2 (line \1)/' |
  grep '\(^-\|[^^] (line \)' |
  sed "s:^- $root/:- :" |
  sed 's/ *\* *\(.*\) (line \([^)]*\))/\2: \1/' |
  sort -u | sort -n
exit $status
