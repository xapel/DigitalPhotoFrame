#!/usr/bin/env python3

import my_ina219

ina219 = my_ina219.INA219(addr=0x43)
p = ina219.get_battery_percentage()
print("Battery:       {:3.1f}%".format(p))

# Open the file in write mode
with open('battery.txt', 'w') as file:
    # Write the float as a string to the file
    file.write(f"{p:.1f}")