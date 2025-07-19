#!/usr/bin/env python3
import i3ipc
import os

i3 = i3ipc.Connection()
last_focused_id = None
tmpfile = f"/run/user/{os.getuid()}/last_focused_window"

def on_window_focus(i3, e):
    global last_focused_id
    current = i3.get_tree().find_focused()
    if current.window and current.id != last_focused_id:
        last_focused_id = current.id
        os.makedirs(os.path.dirname(tmpfile), exist_ok=True)
        with open(tmpfile, "w") as f:
            f.write(str(last_focused_id))

i3.on("window::focus", on_window_focus)
i3.main()
