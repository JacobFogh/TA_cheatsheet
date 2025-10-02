def wind_chill(temp, speed):
    #temp = round(temp)
    #speed = round(speed)
    T_wc = 13.12 + 0.6215 * temp - 11.37 * speed**(0.16) + 0.3965 * temp * speed**(0.16)
    return f"{round(temp)}°C with a wind speed of {round(speed)} km/h feels like {round(T_wc)}°C."