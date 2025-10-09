def arrival_times(schedule, delay):
    result = []
    for t in schedule:
        h, m = map(int, t.split(":"))
        total = h * 60 + m
        total = (total + delay) % (24 * 60)     # håndterer evt. næste dag
        hh = total // 60
        mm = total % 60
        result.append(f"{hh:02d}:{mm:02d}")
    return result

print(arrival_times(['12:37', '08:10'], 25))


