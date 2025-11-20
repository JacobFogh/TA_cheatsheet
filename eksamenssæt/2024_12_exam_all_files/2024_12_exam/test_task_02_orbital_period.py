import math
from orbital_period import orbital_period

returned = orbital_period(1.5 * 10**11, 2 * 10**30)
expected = 31593584.1373

if not math.isclose(returned, expected):
    print('Test for task 2 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 2 passed')