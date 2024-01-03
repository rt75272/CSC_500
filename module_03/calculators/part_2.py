HOURS_PER_DAY = 24

current_time = int(input("What time is it(in hours)? "))

alarm_duration = int(input("In how many hours would you like the alarm to go off? "))

alarm_target = (current_time + alarm_duration) % HOURS_PER_DAY
alarm_target = str(alarm_target) + ":00"

print("Your alarm will go off at", alarm_target)