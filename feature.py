import math

# 🔤 Typing speed
def typing_speed(data):
    if len(data) < 2:
        return 0
    return len(data) / (data[-1]['release_time'] - data[0]['press_time'])

# 🔤 Average hold time
def avg_hold_time(data):
    if not data:
        return 0
    return sum(k['hold_time'] for k in data) / len(data)

# 🔤 Flight time (gap between keys)
def flight_time(data):
    gaps = []
    for i in range(1, len(data)):
        gap = data[i]['press_time'] - data[i-1]['release_time']
        gaps.append(gap)
    return sum(gaps)/len(gaps) if gaps else 0

# 🔤 Total key count
def total_keys(data):
    return len(data)

# 🔤 Typing consistency (variance)
def typing_variance(data):
    speeds = [k['hold_time'] for k in data]
    if len(speeds) < 2:
        return 0
    mean = sum(speeds)/len(speeds)
    return sum((x-mean)**2 for x in speeds)/len(speeds)

# 🖱️ Mouse distance
def mouse_distance(data):
    dist = 0
    for i in range(1, len(data)):
        dx = data[i]['x'] - data[i-1]['x']
        dy = data[i]['y'] - data[i-1]['y']
        dist += math.sqrt(dx**2 + dy**2)
    return dist

# 🖱️ Click frequency
def click_frequency(data):
    return len(data)

# 🖱️ Idle time
def idle_time(data):
    gaps = []
    for i in range(1, len(data)):
        gap = data[i]['time'] - data[i-1]['time']
        if gap > 2:  # 2 sec gap = idle
            gaps.append(gap)
    return sum(gaps) if gaps else 0