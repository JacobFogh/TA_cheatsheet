from Wind_chill import wind_chill

expected = "10°C with a wind speed of 25 km/h feels like 6°C."
output = wind_chill(9.6, 25)
if output != expected:
    print("Failed test with wind_chill(9.6, 25) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("passed")

expected = "0°C with a wind speed of 100 km/h feels like -10°C."
output = wind_chill(0.1, 100)
if output != expected:
    print("Failed test with wind_chill(0, 100) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("passed")

expected = "40°C with a wind speed of 0 km/h feels like 38°C."
output = wind_chill(40, 0)
if output != expected:
    print("Failed test with wind_chill(40, 0) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("passed")

expected = "40°C with a wind speed of 20 km/h feels like 45°C."
output = wind_chill(40, 20)
if output != expected:
    print("Failed test with wind_chill(40, 20) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("passed")
