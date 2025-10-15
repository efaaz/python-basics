"""Problem: Smart thermostat alert
Simulate a simple thermostat/device monitor. The program has a device status
and a temperature reading. If the device is 'active' and the temperature is
above 35 degrees, print a high temperature alert. If the device is active and
temperature is normal (<= 35), print that temperature is normal. If the
device is not active, print that the device is offline.
"""

isActive = "active"
temp = 35
if isActive == "active":
    if temp >= 35:
        print("High tempreture alert!")
    else:
        print("Normal tempreture")
else:
    print("Device is not active")