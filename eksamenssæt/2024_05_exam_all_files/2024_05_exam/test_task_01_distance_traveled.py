import math
from distance_traveled import distance_traveled

returned = distance_traveled(5.5)
expected = 148.37625

if math.isclose(returned, expected):
    print(f"Test for task 1 passed")
else:
    print(f"Test for task 1 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
