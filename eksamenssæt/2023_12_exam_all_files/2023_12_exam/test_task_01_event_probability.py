import math
from event_probability import event_probability

returned = event_probability(100, 25)
expected = 0.22217864060085335

if math.isclose(returned, expected):
    print("Test for task 1 passed")
else:
    print("Test for task 1 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))