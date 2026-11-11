#!/usr/bin/env bash
# Renders the showcase preview images (after.jpg, before.jpg) from the HTML
# pages in docs/showcase. The images are build output and are not committed:
# the Pages workflow runs this before it publishes, and you can run it locally
# to preview the site.
#
#   .github/scripts/build-previews.sh           render the missing images
#   .github/scripts/build-previews.sh --force   render all of them again
#
# Needs Chrome or Chromium, and either ImageMagick or macOS sips.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
force="${1:-}"

chrome=""
for c in "${CHROME:-}" google-chrome google-chrome-stable chromium chromium-browser \
         "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
  [ -n "$c" ] || continue
  if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then chrome="$c"; break; fi
done
[ -n "$chrome" ] || { echo "Chrome not found. Set CHROME to its path." >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

to_jpg() { # png in, jpg out, 1000px wide
  if command -v magick >/dev/null 2>&1; then
    magick "$1" -resize 1000x -quality 82 "$2"
  elif command -v convert >/dev/null 2>&1; then
    convert "$1" -resize 1000x -quality 82 "$2"
  elif command -v sips >/dev/null 2>&1; then
    sips -s format jpeg -s formatOptions 82 --resampleWidth 1000 "$1" --out "$2" >/dev/null
  else
    echo "Need ImageMagick or sips to write JPEGs." >&2; exit 1
  fi
}

shot() { # html in, jpg out
  "$chrome" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --user-data-dir="$tmp/profile" --window-size=1280,800 \
    --virtual-time-budget=6000 --screenshot="$tmp/shot.png" "file://$1" >/dev/null 2>&1
  [ -s "$tmp/shot.png" ] || { echo "No screenshot for $1" >&2; exit 1; }
  to_jpg "$tmp/shot.png" "$2"
  rm -f "$tmp/shot.png"
}

n=0
for dir in "$root"/docs/showcase/*/; do
  for pair in index.html:after.jpg before.html:before.jpg; do
    src="$dir${pair%%:*}"; out="$dir${pair##*:}"
    [ -f "$src" ] || { echo "Missing $src" >&2; exit 1; }
    if [ "$force" = "--force" ] || [ ! -s "$out" ]; then
      shot "$src" "$out"; n=$((n+1))
      echo "rendered ${out#"$root"/}"
    fi
  done
done
echo "$n image(s) rendered."
