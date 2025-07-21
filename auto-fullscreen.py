#!/usr/bin/env python3
import i3ipc
import time
import threading

i3 = i3ipc.Connection()
window_states = {}

# Lock for thread safety
from threading import Lock
state_lock = Lock()

# Helper: Set fullscreen after a small delay (window becomes stable)
def set_fullscreen_later(window_id, delay=0.05):
    time.sleep(delay)
    with state_lock:
        window_states[window_id] = True
    i3.command(f'[con_id="{window_id}"] fullscreen enable')

# New window handler
def on_new_window(i3, e):
    win = e.container
    if win.window:  # Check if it's a real window
        threading.Thread(target=set_fullscreen_later, args=(win.id,)).start()

# Focused window change handler
def on_window_focus(i3, e):
    win = e.container
    if win.id is None or not win.window:
        return

    with state_lock:
        state = window_states.get(win.id, True)  # Default is fullscreen
    cmd = "enable" if state else "disable"
    i3.command(f'[con_id="{win.id}"] fullscreen {cmd}')

# Keybinding handler for F11
def on_binding(i3, e):
    if 'F11' in e.binding.symbol:
        focused = i3.get_tree().find_focused()
        if focused and focused.window:
            with state_lock:
                current_state = window_states.get(focused.id, True)
                new_state = not current_state
                window_states[focused.id] = new_state
            cmd = "enable" if new_state else "disable"
            i3.command(f'[con_id="{focused.id}"] fullscreen {cmd}')

# Register handlers
i3.on("window::new", on_new_window)
i3.on("window::focus", on_window_focus)
i3.on("binding", on_binding)

# Start the event loop
i3.main()

