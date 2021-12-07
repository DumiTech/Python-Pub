"""
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""

#thinking to change the hours in seconds until the final result, like a UNIX timestamp of the current day(starting from today)
hour = 3600 #s
time_0 = 6.52 * hour    #genesis

distance_1 = 1 #mile
velocity_1 = 8.15 #mile/h
time_1 = distance_1 * hour / velocity_1 #s
time_status_1 = time_0 + time_1 #s

distance_2 = 3 #miles
velocity_2 = 7.12 #miles/h
time_2 = distance_2 * hour / velocity_2 #s
time_status_2 = time_status_1 + time_2  #s

distance_3 = 1 #mile
velocity_3 = velocity_1
time_3 = distance_3 * hour / velocity_3 #s
time_status_3 = time_status_2 + time_3

time_f = round(time_status_3 / hour, 2)

#final time converted back to normal
if time_f <= 12:
    print(f'{time_f} AM')
elif time_f >= 13 and time_f < 24:
    print(f'{time_f} PM')
else:
    print('\n##### Something went wrong regarding the time #####')