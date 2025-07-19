#!/usr/bin/env python3
import i3ipc
import json
import os

TRACK_FILE = "/tmp/last_focused_window"

# Load stack if exists
if os.path.exists(TRACK_FILE):
    try:
        with open(TRACK_FILE, "r") as f:
            stack = json.load(f)
    except Exception:
        stack = []
else:
    stack = []

i3 = i3ipc.Connection()

def on_window_focus(i3, e):
    global stack
    current = i3.get_tree().find_focused()
    if current.window:
        if stack and stack[-1] == current.id:
            return  # No change, same window focused
        stack.append(current.id)
        # Keep only last 2
        stack = stack[-2:]
        with open(TRACK_FILE, "w") as f:
            json.dump(stack, f)

i3.on("window::focus", on_window_focus)
i3.main()
