import os
from nitrate_levels import nitrate_levels

filename = 'files/nitrate_data_A.txt'
file_exists = os.path.isfile(filename)
if file_exists:

    returned = nitrate_levels('files/nitrate_data_A.txt')
    expected = (0, 0, 8, 2, 0)

    if returned == expected:
        print(f"Test for task 9 passed")
    else:
        print(f"Test for task 9 failed because it returned:")
        print(repr(returned))
        print("instead of")
        print(repr(expected))
else:
    print("Test for task 9 failed because the filename is not pointing to a valid file.")
