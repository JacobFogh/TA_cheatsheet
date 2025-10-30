from reversed_text import reversed_text

returned = reversed_text('Hello world we are going to do some programming', 'letters')
expected = 'olleH dlrow ew era gniog ot od emos gnimmargorp'

if returned == expected:
    print(f"Test for task 3 passed")
else:
    print(f"Test for task 3 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
