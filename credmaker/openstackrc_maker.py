#!/usr/bin/env python3

outfile=open("admin.rc","a")
osAUTH=input("What is the OS_AUTH_URL? ")
print("export OS_AUTH_URL="+osAUTH,file=outfile)

print("export OS_IDENTITY_API_VERSION=3", file=outfile)

osPROJ = input("What is the OS_PROJECT_NAME? ")
print("export OS_PROJECT_NAME=" + osPROJ, file=outfile)

osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outfile)

osUSER = input("What is the OS_USERNAME? ")
print("export OS_USERNAME=" + osUSER, file=outfile)

osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outfile)

osPASS = input("What is the OS_PASSWORD? ")
print("export OS_PASSWORD=" + osPASS, file=outfile)
outfile.close()
