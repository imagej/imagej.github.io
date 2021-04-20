#!/bin/sh

pages=$(cd "$(dirname "$0")/../_pages" && pwd)
for f in "$pages/users/"*
do
  user=${f##*/}
  user=${user%.md}
  github=$(grep -o "github: .*" "$f")
  github=${github#github: }
  test "$github" -a "$github" != "$user" &&
    echo "$user: GitHub ID mismatch: $github"
done
