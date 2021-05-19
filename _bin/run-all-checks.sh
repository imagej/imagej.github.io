#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
bin="$dir/_bin"
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

echo "[Checking user IDs]"
"$bin/check-user-ids.sh"
test $? -eq 0 && echo "--> User IDs look good."

echo
echo "[Checking include usage]"
"$bin/check-include-usage.sh"
test $? -eq 0 && echo "--> Includes look good."

echo
echo "[Checking include documentation]"
"$bin/check-include-help.sh"
test $? -eq 0 && echo "--> Include docs look good."

echo
echo "[Checking HTML element id values]"
"$bin/check-html-ids.sh"
test $? -eq 0 && echo "--> HTML element ids look good."

echo
echo "[Checking site HTML]"
"$bin/check-site-html.sh"
test $? -eq 0 && echo "--> Site HTML looks good! Congratulations."
