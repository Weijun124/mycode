#!/usr/bin/env python3

switch={"hostname":"sw1","ip":"10.0.1.1","version":"1.2", "vendor":"cisco"}
print(switch["hostname"])
print(switch["ip"])
print(switch,"\n")

# print(switch["lynx"])

print("First test - .get()")
print(switch.get("lynx"),"\n")

print("Second test - .get()")
print(switch.get("lynx", "The KEY is in another castle!"),"\n")

print("Third test - .get()")
print(switch.get("version"),"\n")

print("Sixth test - .pop()")
switch.pop("version") # removes this key (and value) pair
print(switch.keys())  # version is gone
print(switch.values(),"\n") # value 1.2 is gone 

print("Seventh test - ADD a mew value")
switch["adminlogin"]="karl08"
print(switch.keys())
print(switch.values(),"\n")

print("Eighth test - ADD a new value")
switch["password"]="qwerty"
print(switch.keys())
print(switch.values())

