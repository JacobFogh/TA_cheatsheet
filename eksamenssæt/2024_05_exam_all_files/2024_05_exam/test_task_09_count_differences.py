import os
from count_differences import count_differences

filename1 = 'files/results_A1.txt'
filename2 = 'files/results_A2.txt'

files_exist = os.path.isfile(filename1) and os.path.isfile(filename2)  

if files_exist:

    returned = count_differences(filename1, filename2)
    expected = 3

    if returned == expected:
        print(f"Test for task 9 passed")
    else:
        print(f"Test for task 9 failed because it returned:")
        print(repr(returned))
        print("instead of:")
        print(repr(expected))
else:
    print("Test for task 9 failed because the filenames are not pointing to valid files.")
