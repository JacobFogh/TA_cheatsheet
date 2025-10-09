from collatz_conjecture import collatz_conjecture

returned = collatz_conjecture(3)
expected = 7

if returned == expected:
    print(f"Test for task 6 passed")
else:
    print(f"Test for task 6 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
