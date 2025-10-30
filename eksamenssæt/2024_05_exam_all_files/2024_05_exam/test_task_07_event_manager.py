from event_manager import EventManager

my_event = EventManager()
returned1 = my_event.get_num_registrations()
returned2 = my_event.deregister('Mike')
returned3 = my_event.register('Mike')
returned4 = my_event.register('Mike')
returned5 = my_event.register('John')
returned6 = my_event.deregister('Mike')
returned7 = my_event.get_num_registrations()

expected1 = 0
expected2 = False
expected3 = True
expected4 = False
expected5 = True
expected6 = True
expected7 = 1

if ((returned1 == expected1) and (returned2 == expected2) and
        (returned3 == expected3) and (returned4 == expected4) and
        (returned5 == expected5) and (returned6 == expected6) and 
        (returned7 == expected7)):
    print(f"Test for task 7 passed")
else:
    print(f"Test for task 7 failed because it yielded:")
    print(repr(returned1), repr(returned2), repr(returned3), repr(returned4), 
            repr(returned5), repr(returned6), repr(returned7))
    print("instead of:")
    print(repr(expected1), repr(expected2), repr(expected3), repr(expected4),
            repr(expected5), repr(expected6), repr(expected7))



