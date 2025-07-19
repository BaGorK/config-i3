#!/usr/bin/env python3
import i3ipc
import os
import sys

tmpfile = f"/run/user/{os.getuid()}/last_focused_window"

try:
    with open(tmpfile, "r") as f:
        last_id = f.read().strip()
except FileNotFoundError:
    sys.exit(1)

i3 = i3ipc.Connection()
i3.command(f'[con_id="{last_id}"] focus')
