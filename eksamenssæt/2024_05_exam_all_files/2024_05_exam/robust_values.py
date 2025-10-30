import numpy as np

def robust_values(x):
    mean = np.mean(x)
    std = np.std(x)

    upper_bound = mean + std
    lower_bound = mean - std


    new_array = []

    for i in x:
        if i > lower_bound and i < upper_bound:
            new_array.append(i)

    return np.array(new_array)

x = np.array([41.42, 44.32, 45.56, 63.01, 12.22, 42.82, 43.73, 40.11])

print(robust_values(x))