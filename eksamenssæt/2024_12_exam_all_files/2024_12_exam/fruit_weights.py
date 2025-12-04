import numpy as np


def fruit_weights(table):
    new_table = {}
    for i in table:
        if i.lower() not in new_table:
            new_table[i.lower()] = [table[i]]
        else:
            new_table[i.lower()].append(table[i])

    final_weight = {i : np.floor(np.mean(new_table[i])) for i in new_table}
    
    return final_weight


table = {'apple': 182,
         'banana': 110,
         'Orange': 160,
         'Banana': 115,
         'APPLE': 185,
         'Apple': 175,
         'lime': 67}

print(fruit_weights(table))