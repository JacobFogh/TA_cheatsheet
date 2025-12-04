def traffic_operation(hour):
    if (hour > 7 and hour < 9) or (hour > 15 and hour < 17):
        return "rush hour"
    elif hour > 22 and hour < 6:
        return "night time"
    else:
        return "normal"
    


print(traffic_operation(8))