#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll build"
  exit 1
}

error() { echo "$*" >&2; }

FLAGS=--disable-external
VERBOSE=
while [ $# -gt 0 ]
do
  case "$1" in
    -x|--check-external-links) FLAGS= ;;
    -v|--verbose) VERBOSE=1 ;;
    -*) error "Ignoring unknown switch: $1" ;;
    *) test -z "$F" && F=$1 || error "Ignoring extra argument: $1" ;;
  esac
  shift
done

test "$F" || { error "No filename given." && exit 1; }

output=$(bundle exec htmlproofer "$F" \
  --allow-hash-href \
  --assume-extension \
  --check-html \
  --check-img-http \
  --check-opengraph \
  $FLAGS \
  --empty-alt-ignore \
  --report-invalid-tags \
  --report-missing-names \
  --report-script-embeds \
  --report-missing-doctype \
  --report-eof-tags \
  --report-mismatched-tags \
  --url-ignore \"/^/ij$/,/^/conference$/,/^/list-of-update-sites$/,/^/mbf$/,/^/presentations$/,/^/tickets$/,/^/workshops$/,/^/images$/,/^/ij//,/^/conference//,/^/list-of-update-sites//,/^/mbf//,/^/presentations//,/^/tickets//,/^/workshops//,/^/images//\" \
  --root-dir="$root" 2>&1)
status=$?
test "$VERBOSE" && echo "$output" ||
  echo "$output" |
    sed 's/ *\* *\([0-9][0-9]*:[0-9][0-9]*\):* *\(.*\)/  *  \2 (line \1)/' |
    grep '\(^-\|[^^] (line \)' |
    sed "s:^- $root/:- :" |
    sed 's/ *\* *\(.*\) (line \([^)]*\))/\2: \1/' |
    sort -u | sort -n
exit $status
