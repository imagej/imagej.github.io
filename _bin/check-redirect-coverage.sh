#!/bin/sh

for mw in $(git ls-tree --name-only mediawiki-final | grep '\.mw$' | grep -v '^\(File\|Template\|Talk\|Category\|MediaWiki\):' | sed 's:%2F:/:g')
do
  page=${mw%.mw}
  grep -q "^$page :: " redirects.txt || echo "$page"
done
