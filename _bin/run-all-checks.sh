#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
bin="$dir/_bin"
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll build"
  exit 1
}

errors=0

echo "[Checking page generation]"
"$bin/check-page-generation.sh" &&
   echo "--> Page generation looks good." ||
  errors=$((errors+$?))

echo
echo "[Checking user IDs]"
"$bin/check-user-ids.sh" &&
  echo "--> User IDs look good." ||
  errors=$((errors+$?))

echo
echo "[Checking include usage]"
"$bin/check-include-usage.sh" &&
  echo "--> Includes look good." ||
  errors=$((errors+$?))

echo
echo "[Checking include documentation]"
"$bin/check-include-help.sh" &&
  echo "--> Include docs look good." ||
  errors=$((errors+$?))

echo
echo "[Checking HTML element id values]"
"$bin/check-html-ids.sh" &&
  echo "--> HTML element ids look good." ||
  errors=$((errors+$?))

# NB: Disabled until check-page-html.sh caches its output
# for the same input hash. Once that's in place, running
# this test on CI won't be so super expensive.
#echo
#echo "[Checking site HTML]"
#"$bin/check-site-html.sh" &&
#  echo "--> Site HTML looks good! Congratulations." ||
#  errors=$((errors+$?))

test "$errors" -gt 255 && errors=255
exit $errors
