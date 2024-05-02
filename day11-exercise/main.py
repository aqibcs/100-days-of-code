import time

# Get the current time in hours
current_hour = int(time.strftime('%H'))

# Determine whether it's morning, afternoon, or evening
if current_hour < 12:
    time_of_day = "Morning"
elif current_hour < 17:
    time_of_day = "Afternoon"
else:
    time_of_day = "Evening"

# Get the timestamp with AM/PM format
timestamp = time.strftime('%I:%M:%S %P')

# Combine the timestamp and time of day
formatted_time = f"{timestamp} {time_of_day}"

print(formatted_time)
