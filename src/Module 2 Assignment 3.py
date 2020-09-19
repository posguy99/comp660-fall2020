#!/usr/bin/env python3

kg_to_lb = 2.20462
earth_grav = 9.807  # m/s^2
moon_grav = 1.62   # m/s^2

mass = float(input("Please enter the mass in lb that you would like to convert to kg: "))
kg = mass / kg_to_lb

print("The converted mass in kg is:", kg)
print("Your weight on Earth is:", kg*earth_grav, "Newtons")
print("Your weight on the Moon is:", kg*moon_grav, "Newtons")
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth:", (kg*moon_grav)/(kg*earth_grav)*100, "%")
print("The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer:", round((kg*moon_grav)/(kg*earth_grav)*100), "%")
