#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""
with open("dnsservers.txt", "r") as dnsfile:

    for svr in dnsfile:
        svr = svr.rstrip('\n')
        print(svr)

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")
