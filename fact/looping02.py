#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

def main():
    dnsfile=open("dnsservers.txt","r")
    dnslist=dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")
    dnsfile.close()
main()

# you can also use "with" function to wrap open and end
"""with open("dnsservers.txt","r") as dnsfile:
    dnslist = dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")"""
