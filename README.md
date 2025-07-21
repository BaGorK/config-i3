---

## 🧠 My i3wm Config

A highly customized [i3 Window Manager](https://i3wm.org/) configuration optimized for fullscreen productivity, fast navigation, and keyboard-centric workflows.

---

### 🚀 Features

#### 1. 🔲 **Auto Fullscreen Mode**

* Every new window (except Firefox) opens in **fullscreen** by default.
* Firefox is excluded from auto-fullscreen for better tab and window management.
* Toggling fullscreen via `F11` updates the state persistently.

#### 2. 🧭 **Focus Tracker & Focus Last**

* Tracks the **last focused** window using `i3ipc`.
* Press `$mod + ,` to return to the last focused window instantly.

#### 3. ⌨️ **Smart Keybindings**

* `$mod + space`: Switch between windows using `rofi`.
* `$mod + n`: Application launcher (`rofi drun`).
* `$mod + c`: Run command dialog.
* `$mod + f`: File browser mode via `rofi`.

#### 4. 🖼️ **Autostart Applications**

* Automatically launches:

  * `gnome-terminal`
  * `firefox`
  * `telegram-desktop`
* Then switches to **Workspace 3**.

#### 5. 🌐 **Language & Input Customization**

* Keyboard toggle: `English` ↔ `Amharic` via `Alt + Shift`.
* Caps Lock remapped to `Escape`.

#### 6. 🔆 **Utilities**

* `F5/F6`: Brightness control.
* `Print`: Screenshots with `flameshot`.
* `$mod + Ctrl + R`: Screen recording with `ffmpeg`.

---

### 📜 Scripts

* **`auto-fullscreen.py`**:

  * Fullscreen toggle and tracking per window.
  * Remembers fullscreen state when switching between windows.
  * Ignores Firefox.

* **`focus-tracker.py`**:

  * Stores the ID of the last focused window.

* **`focus-last.py`**:

  * Switches back to the previously focused window when `$mod + ,` is pressed.

---

### 🔧 Dependencies

Install these Python packages:

```bash
pip install i3ipc
```

Optional (but recommended):

```bash
sudo pacman -S rofi flameshot xdotool brightnessctl ffmpeg
```

---

### 🖼️ Wallpaper

Automatically sets your background using `feh`:

```bash
feh --bg-fill ~/Pictures/pc-wallpaper/image-5.jpg
```

---

### 📂 Directory Structure

```bash
~/.config/i3/
├── config              # Your main i3 config file
├── auto-fullscreen.py # Fullscreen handler with state memory
├── focus-tracker.py   # Tracks focused window ID
├── focus-last.py      # Switch back to last focused window
```

---
