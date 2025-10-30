from event_manager import LimitedEventManager

my_event = LimitedEventManager(3)
returned1 = my_event.register('Mike')
returned2 = my_event.register('Emily')
returned3 = my_event.register('Sara')
returned4 = my_event.register('Peter')
returned5 = my_event.get_num_registrations()

expected1 = True
expected2 = True
expected3 = True
expected4 = False
expected5 = 3

if ((returned1 == expected1) and (returned2 == expected2) and
        (returned3 == expected3) and (returned4 == expected4) and
        (returned5 == expected5)):
    print(f"Test for task 10 passed")
else:
    print(f"Test for task 10 failed because it returned:")
    print(repr(returned1), repr(returned2), repr(returned3), repr(returned4), 
        repr(returned5))
    print("instead of:")
    print(repr(expected1), repr(expected2), repr(expected3), repr(expected4), 
        repr(expected5))