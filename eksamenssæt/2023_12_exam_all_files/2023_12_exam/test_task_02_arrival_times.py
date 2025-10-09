from arrival_times import arrival_times

returned = arrival_times(['12:37', '08:10'], 25)
expected = ['13:02', '08:35']

if returned == expected:
    print("Test for task 2 passed")
else:
    print("Test for task 2 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))