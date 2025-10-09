def arrival_times(schedule, delay):
    arrival_string = [i.split(':') for i in schedule]
    arrival_numbers = []
    print(arrival_string)

print(arrival_times(['12:37', '08:10'], 25))


