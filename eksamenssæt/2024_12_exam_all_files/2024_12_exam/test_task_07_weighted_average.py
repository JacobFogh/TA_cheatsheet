import numpy as np
import math
from weighted_average import weighted_average

returned = weighted_average(np.array([4.8, 6.6, 12.2, 7.3, 6.5]))
expected = 6.748513328262833

if not math.isclose(returned, expected):
    print('Test for task 7 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 7 passed')