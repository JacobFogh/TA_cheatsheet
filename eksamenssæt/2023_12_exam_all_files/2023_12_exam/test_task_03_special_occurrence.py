from special_occurrence import special_occurrence

returned = special_occurrence([2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6])
expected = 11

if returned == expected:
    print("Test for task 3 passed")
else:
    print("Test for task 3 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))