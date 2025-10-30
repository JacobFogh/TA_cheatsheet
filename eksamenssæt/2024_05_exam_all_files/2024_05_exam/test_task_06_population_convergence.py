from population_convergence import population_convergence

returned = population_convergence(4.8, 0.65)
expected = 6

if returned == expected:
    print(f"Test for task 6 passed")
else:
    print(f"Test for task 6 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
