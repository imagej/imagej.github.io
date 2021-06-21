#!/bin/sh

# Scans for unused and unknown classes.

root=$(cd "$(dirname "$0")/../_site" && pwd)
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

cd "$root"

cssfiles="
assets/css/main.css
assets/css/layout.css
assets/css/includes.css
assets/css/timeline.css
assets/css/dock.css
assets/css/noscript.css
assets/css/home.css
assets/css/page.css
"

thirdpartycss="
assets/css/fontawesome-all.min.css
assets/css/lightbox.min.css
assets/css/syntax-highlight-fruity.css
assets/css/syntax-highlight-github.css
"

list_classes() {
  grep -oh '\(^\|[^0-9:-]\)\.[a-zA-Z0-9_-]\+' $@ |
  tr ' ' '\n' |
  sed 's/^[^\.]\?\.//' |
  grep -v '[0-9]em$' |
  sort -u
}

our_classes=$(list_classes $cssfiles)
their_classes=$(list_classes $thirdpartycss)

usages=$(grep -IRoh ' class="[^"]*"' |
  sed 's/^[^"]*"\(.*\)"$/\1/g' |
  tr ' ' '\n' |
  grep -v '[^A-Za-z0-9_-]' |
  sort -u)

errors=0

for class in $(echo "$our_classes")
do
  echo "$usages" | grep -q "^$class$" ||
    { echo "Unused class: $class"; errors=$((errors+1)); }
done

for usage in $(echo "$usages")
do
  { echo "$our_classes"; echo "$their_classes"; } | grep -q "^$usage$" ||
    { echo "Unknown class: $usage"; errors=$((errors+1)); }
done

test "$errors" -gt 255 && errors=255
exit $errors
