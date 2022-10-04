#!/usr/bin/env python3

import os

def find(name,path):
    for root,dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root,name)
lookfor=input('what am I looking for?')
lookwhere=input("What is the path in which I should serarch? ")

print(find(lookfor, lookwhere))
