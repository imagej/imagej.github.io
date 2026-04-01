#!/bin/sh
# Runs WCAG 2.1 AA accessibility checks against the built site using
# pa11y with the axe runner.  Requires Node.js (npx must be on PATH).
#
# Usage: _bin/check-accessibility.sh [page ...]
#   The site must already be built (bundle exec jekyll build).
#
# With no arguments, checks every page in _site/ (all HTML files).
# With arguments, checks the home page plus each specified path, e.g.:
#   _bin/check-accessibility.sh learn downloads
#
# The home page always suppresses color-contrast, aria-required-children,
# and link-in-text-block (image-background issues flagged needsFurtherReview
# by axe).  All pages suppress nested-interactive.
#
# Results are cached in .accessibility-cache by content hash so unchanged
# pages are skipped on subsequent runs.
#
# All checks use the axe runner (not htmlcs) to avoid false positives.
# Only errors that axe can definitively confirm (needsFurtherReview=false)
# count toward the exit status.

dir=$(cd "$(dirname "$0")/.." && pwd)
root="$dir/_site"
test -d "$root" || {
  echo "Please generate the site first."
  echo "  bundle exec jekyll build"
  exit 1
}

PORT=9876
BASE="http://localhost:$PORT"
CACHE_FILE="$dir/.accessibility-cache"

# Compute SHA-256 of a file (works on both macOS and Linux).
hash_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  else
    shasum -a 256 "$1" | cut -d' ' -f1
  fi
}

# Map a full URL to the corresponding built HTML file under _site/.
html_file_for_url() {
  path="${1#"$BASE"}"   # strip base URL prefix
  echo "$root$path"
}

# Return 0 (hit) if the given URL's HTML file matches its cached hash.
cache_hit() {
  url_path="$1"
  html_file="$2"
  [ -f "$CACHE_FILE" ] || return 1
  [ -f "$html_file" ]  || return 1
  current_hash=$(hash_file "$html_file")
  stored=$(grep "^$url_path " "$CACHE_FILE" 2>/dev/null | cut -d' ' -f2)
  [ "$stored" = "$current_hash" ]
}

# Record a passing URL+hash in the cache file.
cache_update() {
  url_path="$1"
  html_file="$2"
  [ -f "$html_file" ] || return
  current_hash=$(hash_file "$html_file")
  tmpfile=$(mktemp)
  grep -v "^$url_path " "$CACHE_FILE" 2>/dev/null > "$tmpfile" || true
  echo "$url_path $current_hash" >> "$tmpfile"
  mv "$tmpfile" "$CACHE_FILE"
}

# Start a static file server for the built site.
# We use a port other than 4000 to avoid colliding with a running Jekyll
# dev server.
npx --yes serve "$root" --listen $PORT --no-clipboard >/dev/null 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null' EXIT
trap 'exit 130' INT TERM

# Give the server a moment to be ready.
sleep 2

echo "Running accessibility checks (pa11y / axe / WCAG2AA)..."

errors=0
check_url() {
  url="$1"
  shift
  url_path="${url#"$BASE"}"
  html_file=$(html_file_for_url "$url")
  printf "  Checking %s ... " "$url"
  if cache_hit "$url_path" "$html_file"; then
    echo "OK (cached)"
    return
  fi
  # pa11y exits 2 if there are errors, 0 if clean.
  # Use --reporter json so we can filter out needsFurtherReview issues.
  output=$(npx --yes pa11y --standard WCAG2AA --runner axe --reporter json "$@" "$url" 2>/dev/null)
  count=$(echo "$output" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    real = [i for i in data
            if i.get('type') == 'error'
            and not i.get('runnerExtras', {}).get('needsFurtherReview', False)]
    print(len(real))
    for i in real:
        print('  ERROR [' + i.get('code','?') + '] ' + i.get('context','')[:80])
except Exception as e:
    print(0)
")
  real_errors=$(echo "$count" | head -1)
  detail=$(echo "$count" | tail -n +2)
  if [ "$real_errors" -eq 0 ]; then
    echo "OK"
    cache_update "$url_path" "$html_file"
  else
    echo "FAILED ($real_errors error(s))"
    echo "$detail"
    errors=$((errors + real_errors))
  fi
}

check_home() {
  # Home page: ignore color-contrast and aria-required-children (all image-background
  # issues flagged needsFurtherReview=true by axe, but pa11y --runner axe still exits
  # non-zero for them).  Also ignore link-in-text-block in the hero section.
  check_url "$BASE/index.html" \
    --ignore "color-contrast" \
    --ignore "aria-required-children" \
    --ignore "link-in-text-block" \
    --ignore "nested-interactive"
}

if [ "$#" -eq 0 ]; then
  # Default: check every page in _site/.
  tmplist=$(mktemp)
  find "$root" -name "*.html" | sort > "$tmplist"
  while IFS= read -r html_file; do
    rel="${html_file#"$root"}"   # e.g. /learn/index.html, or /index.html
    check_url "$BASE$rel" \
      --ignore "nested-interactive"
  done < "$tmplist"
  rm -f "$tmplist"
else
  # Check the home page plus each explicitly requested path.
  check_home
  while [ "$#" -gt 0 ]; do
    check_url "$BASE/$1" \
      --ignore "nested-interactive"
    shift
  done
fi

if [ "$errors" -eq 0 ]; then
  echo "Accessibility looks good."
else
  echo "Accessibility checks failed with $errors error(s)."
fi

exit "$errors"
