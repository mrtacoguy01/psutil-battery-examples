# This script uses a library called "psutil" to check the battery level and charging status of the device.

# Import the psutil library, if not installed you can install it with most python package managers
import psutil

# Set a variable named "battery" to the result of the "psutil.sensors_battery()" function.
# This function returns the battery information of the system.
battery = psutil.sensors_battery()

if battery.secsleft == psutil.POWER_TIME_UNLIMITED:
        time_remaining = "Power plugged in / Unlimited"

elif battery.secsleft == psutil.POWER_TIME_UNKNOWN:
    time_remaining = "Calculating / Unavailable"

else:
    # Convert seconds to hours and minutes
    hours = battery.secsleft // 3600
    minutes = (battery.secsleft % 3600) // 60
    time_remaining = f"{hours}h {minutes}m remaining"

# Print remaining time
print(time_remaining)