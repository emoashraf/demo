from pynput import keyboard, mouse
import time

keystrokes = []
key_press_times = {}
mouse_moves = []
mouse_clicks = []
scrolls = []

# 🔤 Key press
def on_press(key):
    key_press_times[key] = time.time()

# 🔤 Key release (IMPORTANT for hold time)
def on_release(key):
    if key in key_press_times:
        hold = time.time() - key_press_times[key]

        keystrokes.append({
            "key": str(key),
            "press_time": key_press_times[key],
            "release_time": time.time(),
            "hold_time": hold
        })

# 🖱️ Mouse move
def on_move(x, y):
    mouse_moves.append({
        "x": x,
        "y": y,
        "time": time.time()
    })

# 🖱️ Click
def on_click(x, y, button, pressed):
    if pressed:
        mouse_clicks.append({
            "x": x,
            "y": y,
            "time": time.time()
        })

# 🖱️ Scroll
def on_scroll(x, y, dx, dy):
    scrolls.append({
        "dy": dy,
        "time": time.time()
    })

def start_capture():
    k = keyboard.Listener(on_press=on_press, on_release=on_release)
    m = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

    k.start()
    m.start()

    k.join()
    m.join()