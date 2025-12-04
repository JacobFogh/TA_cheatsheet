import os

path = 'files/lines1.txt'
if not os.path.isfile(path):
    print('Test failed because path could not be found.')
    exit(1)


from lines_containing import lines_containing

returned = lines_containing(path, 'a')
expected = 2

if returned != expected:
    print('Test failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test passed')