def reservoir_levels(levels):
    indeks_list = []

    for i in range(len(levels) - 1):
        if (levels[i] - levels[i + 1]) > 150:
            indeks_list.append(i + 1)
    
    return indeks_list

print(reservoir_levels([1320, 1307, 1295, 1102, 1360, 1395, 1101, 1208]))