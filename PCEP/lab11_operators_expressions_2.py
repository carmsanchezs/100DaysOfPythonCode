hours = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hours += (mins + dura) // 60
mins = (mins + dura) % 60

if hours > 24:
    hours_mas = hours // 24
    hours -= hours_mas * 24

print("The time is ", str(hours) + ":" + str(mins))
