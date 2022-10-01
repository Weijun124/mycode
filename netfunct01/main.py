#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons
import json

def commandpush(devicecmd):
    for ip in devicecmd.keys():
        devicereboot(ip)
        print(f'Handshaking......connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
    return None

def devicereboot(ip):
    print(f"\nConnecting to {ip}, REBOOTING NOW!")
    

def main():
    """called at runtime"""
    with open("devicecmd.json","r") as devicecmdjson: 
        devicecmd=json.load(devicecmdjson)

    print(f"Welcome to the {crayons.blue('Netwoek')} Device command pusher")
    print("\nData set found")

   #call the commandpush function and pass the dictionary as parameter
    commandpush(devicecmd)
main()
