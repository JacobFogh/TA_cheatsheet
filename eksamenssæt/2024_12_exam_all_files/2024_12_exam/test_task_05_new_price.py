import math
from new_price import new_price

returned = new_price(143.50, 40)
expected = (86.1, '86.10 DKK')

if len(returned) != len(expected) or not math.isclose(returned[0], expected[0]) or returned[1] != expected[1]:
    print('Test for task 5 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 5 passed')