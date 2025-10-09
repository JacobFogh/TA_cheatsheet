def event_probability(T, n):
    P = 1 - (1 - 1/T)**n
    return P

print(event_probability(100, 25))