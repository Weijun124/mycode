#!/usr/bin/env python3

import re
import urllib.request

def searchfunction(searchFor,searchMe):
    if re.search(searchFor,searchMe):
        print("Found a match!")
    else:
        print("No match!")

def main():
    """Search a website's content"""
    ans='y'
    while ans.lower()=='y':
        print("Where should we search?")
        url=input("> ")
        print(f"Great! So we'll try to open this URL {url} to search for the phrase: ")
        searchFor=input("> ")
        searchMe=urllib.request.urlopen(url).read().decode("utf-8") 
        searchfunction(searchFor,searchMe)    
        ans=input("Do you want to continue? [y/n]")
        
        if ans.lower()!='y':
            break

main()
