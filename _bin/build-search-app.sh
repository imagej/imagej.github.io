#!/bin/sh

# Builds assets/js/search.js app from the source of _search/client.
# Requires node.js to be installed.

root=$(cd "$(dirname "$0")/.." && pwd)

cd "$root/_search/client" &&
rm -rf dist &&
npm run-script build &&
cp dist/app*.js "$root/assets/js/search.js"
