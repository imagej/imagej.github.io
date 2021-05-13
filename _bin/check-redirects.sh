#!/bin/sh

dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

echo "[Any missing redirect definitions?]"
for mw in $(git ls-tree --name-only mediawiki-final | grep '\.mw$' | grep -v '^\(File\|Template\|Talk\|Category\|MediaWiki\):' | sed 's:%2F:/:g')
do
  page=${mw%.mw}
  grep -q "^$page :: " redirects.txt || echo "$page"
done

echo
echo "[Any invalid redirect destinations?]"
tmpfile=redirects.html
echo '<!DOCTYPE html><html><body>' > "$tmpfile"
cat redirects.txt |
  sed '/.* :: \/$/d' | sed '/</d' | sed '/TODO/d' |
  sed 's;.* :: \(.*\);<a href="/\1">\1</a>;' >> "$tmpfile"
echo '</body></html>' >> "$tmpfile"
_bin/check-page-html.sh "$tmpfile"
success=$?
test $success -eq 0 && rm redirects.html
exit $?
