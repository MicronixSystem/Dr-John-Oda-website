#!/usr/bin/env bash
# Hero video: H.264 720p two-pass at ~500 kbps total (about 7.6 MB for 122 s),
# +faststart, plus a WebP poster at 53.4 s (looking straight into the lens).
set -euo pipefail
SITE="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$(ls "$SITE"/_harvest/raw/home-hero-video_*.mp4 | head -1)"
OUT="$SITE/assets/video"
TMP="${TMPDIR:-/tmp}/djo-pass"
mkdir -p "$OUT" "$TMP"

ffmpeg -y -loglevel error -i "$SRC" -vf "scale=-2:720" -c:v libx264 -preset slow \
  -b:v 430k -pass 1 -passlogfile "$TMP/p" -an -f null -
ffmpeg -y -loglevel error -i "$SRC" -vf "scale=-2:720" -c:v libx264 -preset slow \
  -b:v 430k -pass 2 -passlogfile "$TMP/p" -profile:v high -pix_fmt yuv420p \
  -c:a aac -b:a 64k -ac 1 -movflags +faststart "$OUT/dr-john-oda-message.mp4"

ffmpeg -y -loglevel error -ss 53.4 -i "$SRC" -frames:v 1 -vf "scale=1280:-2" \
  -c:v libwebp -quality 82 "$OUT/dr-john-oda-message-poster.webp"
ls -la "$OUT"
