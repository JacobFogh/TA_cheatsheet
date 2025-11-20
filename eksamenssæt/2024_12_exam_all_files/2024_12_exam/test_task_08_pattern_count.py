import os

filename = 'files/dna_data_1.txt'
if not os.path.isfile(filename):
    print('Test for task 8 failed because filename could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct directory in VSCode (as described under `Solving Exam Tasks` in the pdf), or modify the path above.')
    exit()

from pattern_count import pattern_count

returned = pattern_count(filename, 'ACCG')
expected = 2

if returned != expected:
    print('Test for task 8 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 8 passed')