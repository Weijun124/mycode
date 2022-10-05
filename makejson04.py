#!/usr/bin/env python3

import json

def main():
    with open('datacenter.json','r') as datacenter:
        datacenterdecoded=json.load(datacenter)
    print(type(datacenterdecoded))
    print(datacenterdecoded)
    print(datacenterdecoded["row3"])
    print(datacenterdecoded["row2"][1])

if __name__=="__main__":
    main()
