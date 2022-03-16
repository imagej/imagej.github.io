#!/bin/bash

dir=$(cd "$(dirname "$0")/.." && pwd)
bin="$dir/_bin"
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll build"
  exit 1
}

FAIL_FAST=
while [ $# -gt 0 ]
do
  case "$1" in
    --fail-fast) FAIL_FAST=1 ;;
    *) echo "Ignoring extraneous argument: $1" ;;
  esac
  shift
done

errors=0
for f in $(find "$root" -name '*.html'); do
  f=${f#$root}
  f="_site$f"
  "$bin/check-page-html.sh" "$f"
  status=$?
  if [ $status -ne 0 ]
  then
    test "$FAIL_FAST" && exit $status
    errors=$((errors+1))
  else
    sf=$(echo "$f" | sed "s:^$root/::")
    echo "--> $sf OK"
  fi
done
exit $errors
