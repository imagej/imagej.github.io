#!/bin/sh

# Lists files in the media folder that are only used by one folder of _pages
# content, but not residing in the correspondingly named folder under media/.
# These should be moved to the corresponding folder under media/.

find media -type f | while read f
do
sf=${f#media/}
sf=${sf%.*}
current=${f%/*}
current=${current#media}
dirs=$(grep -IR "$sf" _pages | sed 's;/[^/]*:.*;;' | sort -u)
test "$dirs" -a "$(echo "$dirs" | wc -l)" -eq 1 -a "${dirs#_pages}" != "$current" &&
  echo "$dirs :: $f"
done
