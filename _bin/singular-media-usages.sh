#!/bin/sh

# Lists files in the base media/ folder that are only used by one folder of
# _pages content. These should be moved to a corresponding folder under media/

for f in media/*
do
sf=${f#media/}
sf=${sf%.*}
dirs=$(grep -IR "$sf" _pages | sed 's;/[^/]*:.*;;' | sort -u)
test "$dirs" -a "$(echo "$dirs" | wc -l)" -eq 1 && echo "$dirs :: $f"
done
