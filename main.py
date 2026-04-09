from capture import keystrokes, mouse_moves, mouse_clicks, scrolls, start_capture
from feature import *
import json

print("Start typing + mouse actions... CTRL+C to stop")

try:
    start_capture()
except KeyboardInterrupt:
    print("\nStopped!")

    result = {
        "typing_speed": typing_speed(keystrokes),
        "avg_hold_time": avg_hold_time(keystrokes),
        "flight_time": flight_time(keystrokes),
        "total_keys": total_keys(keystrokes),
        "typing_variance": typing_variance(keystrokes),
        "mouse_distance": mouse_distance(mouse_moves),
        "clicks": click_frequency(mouse_clicks),
        "idle_time": idle_time(mouse_moves)
    }

    print(result)

    with open("data.json", "w") as f:
        json.dump(result, f, indent=4)