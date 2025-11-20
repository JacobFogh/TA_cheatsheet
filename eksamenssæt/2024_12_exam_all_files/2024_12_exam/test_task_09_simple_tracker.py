from simple_tracker import SimpleTracker

tracker = SimpleTracker(500)
returned1 = tracker.add(510)
expected1 = False
returned2 = tracker.add(200)
expected2 = True
returned3 = tracker.add(352)
expected3 = True
returned4 = tracker.stats()
expected4 = (552, 152)
tracker.reset()
returned5 = tracker.stats()
expected5 = (0, 0)

if returned1 != expected1:
    print('Test for task 9 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 9 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 9 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 9 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 9 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
else:
    print('Test for task 9 passed')