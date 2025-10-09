import numpy as np
import math
from checkerboard_sum import checkerboard_sum

A = np.array([[ 1.42,  4.0,  55.56, 63.0],
              [ 2.22,  2.22, 33.73, 40.11],
              [12.1,  17.24, 18.0,  33.5],
              [21.15, 14.76, 17.3,  22.1],
              [ 5.34,  6.0,   9.8,   8.18]])
returned = checkerboard_sum(A)
expected = 181.41

if returned == expected:
    print("Test for task 5 passed")
else:
    print("Test for task 5 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))