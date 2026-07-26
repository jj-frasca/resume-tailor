#!/usr/bin/env bash
# Package the skill into dist/resume-tailor.zip for upload to claude.ai.
# Usage: ./build.sh
set -euo pipefail
cd "$(dirname "$0")"

SKILL_DIR="skill/resume-tailor"
OUT="dist/resume-tailor.zip"

[ -f "$SKILL_DIR/SKILL.md" ] || { echo "missing $SKILL_DIR/SKILL.md" >&2; exit 1; }

mkdir -p dist
rm -f "$OUT"

# Zip the skill folder so the archive contains resume-tailor/SKILL.md at its root.
# -x excludes cruft. Run from skill/ so paths inside the zip start at resume-tailor/.
( cd skill && zip -rq "../$OUT" resume-tailor \
    -x '*.DS_Store' '*/__pycache__/*' '*.pyc' )

echo "built $OUT"
unzip -l "$OUT"
