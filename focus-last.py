#!/usr/bin/env python3
import i3ipc
import json

TRACK_FILE = "/tmp/last_focused_window"

try:
    with open(TRACK_FILE, "r") as f:
        stack = json.load(f)
except Exception:
    exit(1)

if len(stack) < 2:
    exit(1)

prev_id = stack[0]  # The one before the current
i3 = i3ipc.Connection()
i3.command(f'[con_id="{prev_id}"] focus')
