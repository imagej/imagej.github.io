#!/bin/sh

# Builds the website into the _site folder, then serves it locally
# at http://127.0.0.1:4000/ so you can preview it in your browser.
# Requires Ruby and Bundler to be installed.

root=$(cd "$(dirname "$0")/.." && pwd)

cd "$root"
bundle exec jekyll clean &&
bundle exec jekyll serve --incremental --profile
