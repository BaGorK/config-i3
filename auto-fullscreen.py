#!/usr/bin/env python3
import i3ipc
import time
import threading

i3 = i3ipc.Connection()

def fullscreen_later(window_id, delay=0.05):
    time.sleep(delay)
    i3.command(f'[con_id="{window_id}"] fullscreen enable')

def on_new_window(i3, e):
    window = e.container
    if window.window:  # Check it's a real X11 window
        threading.Thread(target=fullscreen_later, args=(window.id,)).start()

i3.on("window::new", on_new_window)
i3.main()

