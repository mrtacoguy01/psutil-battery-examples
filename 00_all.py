# This script uses a library called "psutil" to check the battery level and charging status of the device.

# Import the psutil library, if not installed you can install it with most python package managers
import psutil

# Set a variable named "battery" to the result of the "psutil.sensors_battery()" function.
# This function returns the battery information of the system.
battery = psutil.sensors_battery()

# Check if a battery was detected
if battery is not None:

    # Get battery percentage and assign it to a variable named "percent"
    percent = battery.percent

    # Check if the charger is connected and assign the result to a variable named "charging"
    charging = battery.power_plugged

    # Get estimated time left in seconds and assign it to a variable named "secsleft"
    secsleft = battery.secsleft

    # Print battery percentage
    print(f"Battery Level: {percent}%")

    print("")

    # Print charging status
    print(f"Charging: {charging}")

    print("")

    # Print raw time remaining
    # Returns -1 (POWER_TIME_UNLIMITED) when plugged in,
    # or -2 (POWER_TIME_UNKNOWN) if the time cannot be calculated.
    print(f"Time Remaining (Raw): {secsleft}")

    # Convert the time into a custom format and assign it to a variable named "formatted_time"
    if secsleft == psutil.POWER_TIME_UNLIMITED:
        formatted_time = "Power plugged in / Unlimited"

    elif secsleft == psutil.POWER_TIME_UNKNOWN:
        formatted_time = "Calculating / Unavailable"

    else:
        # Convert seconds to hours and minutes
        hours = secsleft // 3600
        minutes = (secsleft % 3600) // 60
        formatted_time = f"{hours}h {minutes}m remaining"

    # Print formatted time remaining
    print(f"Time Remaining (Formatted): {formatted_time}")

    print("")

    # Print the raw battery data
    print("Raw Output:", battery)

else:

    # No battery was found
    print("No battery detected")