#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.local/bin
chmod +x "$DIR/moodterm.py"
ln -sf "$DIR/moodterm.py" ~/.local/bin/moodterm
echo "installed -> ~/.local/bin/moodterm"
