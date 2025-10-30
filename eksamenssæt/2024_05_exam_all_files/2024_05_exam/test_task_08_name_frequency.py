from name_frequency import name_frequency

names = ['Liv Ea Jensen', 
        'Mads Oliver', 
        'Steve Madsen',
        'Anna Simon', 
        'Simon Gade', 
        'Mads Kai Jensen']

returned = name_frequency(names)
expected = {'Liv':1, 'Mads':2, 'Steve':1, 'Anna':1, 'Simon':1}

if returned == expected:
    print(f"Test for task 8 passed")
else:
    print(f"Test for task 8 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
