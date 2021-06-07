#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
bin="$dir/_bin"
root="$dir/_site"
failed=0
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll serve"
  exit 1
}

echo "[Checking page generation]"
"$bin/check-page-generation.sh"
if [ $? -ne 0 ]; then
  failed=$((failed+1))
else
  echo "--> Page generation looks good."
fi

echo
echo "[Checking user IDs]"
"$bin/check-user-ids.sh"
if [ $? -ne 0 ]; then
  failed=$((failed+1))
else
  echo "--> User IDs look good."
fi


echo
echo "[Checking include usage]"
"$bin/check-include-usage.sh"
if [ $? -ne 0 ]; then
  failed=$((failed+1))
else
  echo "--> Includes look good."
fi


echo
echo "[Checking include documentation]"
"$bin/check-include-help.sh"
if [ $? -ne 0 ]; then
  failed=$((failed+1))
else
  echo "--> Include docs look good."
fi


echo
echo "[Checking HTML element id values]"
"$bin/check-html-ids.sh"
if [ $? -ne 0 ]; then
  failed=$((failed+1))
else
  echo "--> HTML element ids look good."
fi


# echo
# echo "[Checking site HTML]"
# "$bin/check-site-html.sh"
# if [ $? -ne 0 ]; then
#   failed=$((failed+1))
# else
#  echo "--> Site HTML looks good! Congratulations."
# fi

echo "$failed checks failed."
exit $failed
