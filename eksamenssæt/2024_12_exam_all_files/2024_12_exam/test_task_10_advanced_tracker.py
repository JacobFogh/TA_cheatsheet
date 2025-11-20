from simple_tracker import AdvancedTracker

tracker = AdvancedTracker(500, 100)
returned1 = tracker.add(200)
expected1 = True
returned2 = tracker.add(352)
expected2 = False
returned3 = tracker.add(252)
expected3 = True
returned4 = tracker.stats()
expected4 = (452, 52)
returned5 = tracker.add(510)
expected5 = False

if returned1 != expected1:
    print('Test for task 10 failed because returned1 was:')
    print(repr(returned1))
    print('instead of:')
    print(repr(expected1))
elif returned2 != expected2:
    print('Test for task 10 failed because returned2 was:')
    print(repr(returned2))
    print('instead of:')
    print(repr(expected2))
elif returned3 != expected3:
    print('Test for task 10 failed because returned3 was:')
    print(repr(returned3))
    print('instead of:')
    print(repr(expected3))
elif returned4 != expected4:
    print('Test for task 10 failed because returned4 was:')
    print(repr(returned4))
    print('instead of:')
    print(repr(expected4))
elif returned5 != expected5:
    print('Test for task 10 failed because returned5 was:')
    print(repr(returned5))
    print('instead of:')
    print(repr(expected5))
else:
    print('Test for task 10 passed')