#!/usr/bin/env python3
import i3ipc

def on_window_focus(i3, e):
    focused = i3.get_tree().find_focused()
    print(f"Focused: name={focused.name}, id={focused.id}, window={focused.window}")

i3 = i3ipc.Connection()
i3.on("window::focus", on_window_focus)
i3.main()
