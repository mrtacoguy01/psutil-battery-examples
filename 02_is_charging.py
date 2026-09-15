# This script uses a library called "psutil" to check the battery level and charging status of the device.

# Import the psutil library, if not installed you can install it with most python package managers
import psutil

# Set a variable named "battery" to the result of the "psutil.sensors_battery()" function.
# This function returns the battery information of the system.
battery = psutil.sensors_battery()

# Print charging status
print(battery.power_plugged)