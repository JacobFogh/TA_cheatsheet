def chamber_pressure(P0, Pmax, Pcrit, k):
    count = 0
    while P0 < Pcrit:
        P0 += k * (Pmax - P0)
        count += 1
    
    return count

print(chamber_pressure(20, 120, 105, 0.1))