from booklet_layout import booklet_layout

returned = booklet_layout(17)
expected = (20, 3)

if returned == expected:
    print(f"Test for task 2 passed")
else:
    print(f"Test for task 2 failed because it returned:")
    print(repr(returned))
    print("instead of:")
    print(repr(expected))
