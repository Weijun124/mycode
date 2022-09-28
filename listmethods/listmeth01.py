#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
print(proto)

print(proto[1])

#split the string to individual element and add to the list
proto.extend("dns")
print(proto)
