#!/bin/sh

# Builds assets/js/search.js app from the source of _search/client.
# Requires node.js to be installed.

root=$(cd "$(dirname "$0")/.." && pwd)

cd "$root/_search/client" &&
rm -rf dist &&
npm run-script build &&
cat dist/app*.js | sed 's;sourceMappingURL=/.*\.map;sourceMappingURL=/assets/js/search.js.map;' > "$root/assets/js/search.js" &&
cat dist/app*.js.map | sed 's;"app\.[0-9a-f]\+\.js";"search.js";' > "$root/assets/js/search.js.map"
