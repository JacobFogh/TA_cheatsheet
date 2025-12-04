import math

def orbital_period(a, M):
    T_2 = ((4 * math.pi**2) / (6.6743 * 10**(-11) * M)) * a**3
    return math.sqrt(T_2)


print(orbital_period(1.5 * 10**11, 2 * 10**30))
#31593584.1373