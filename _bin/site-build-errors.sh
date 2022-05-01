#!/bin/sh

# Displays all site build errors logged via the util/error include.

root=$(cd "$(dirname "$0")/.." && pwd)

cd "$root/_site"
grep -IR 'class="error"' . | sed 's;<div class="notice".*<div class="notice-content">;;'
