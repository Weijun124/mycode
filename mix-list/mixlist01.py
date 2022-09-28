#!/usr/bin/env python3
"""Alta3 Research | TPatrick
    Working with mixed lists"""

def main():
    # Create list
    mylist=["192.168.1.1",5060,"UP"]
    print(mylist)
    # Display the IP address
    print("The first item of the list (IP): "+mylist[0])

    # Display the port
    print("The secont item of the list (port): "+str(mylist[1]))

    # Display the state
    print("The last item of the list (state): "+mylist[2])
    
    # Print out the IP address which is iplist[3:4]
    iplist=[5060,"80",55,"10.0.0.1","10.20.30.1","ssh"]
   
    # Use an "f-string'
    print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
main()
          
