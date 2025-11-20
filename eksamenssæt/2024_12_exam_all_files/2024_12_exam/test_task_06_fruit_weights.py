from fruit_weights import fruit_weights

table = {'apple': 182,
    'banana': 110,
    'Orange': 160,
    'Banana': 115,
    'APPLE': 185,
    'Apple': 175,
    'lime': 67}
returned = fruit_weights(table)
expected = {'apple': 180, 'banana': 112, 'orange': 160, 'lime': 67}

if returned != expected:
    print('Test for task 6 failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for task 6 passed')