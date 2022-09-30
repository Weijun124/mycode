#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    print("This is list of our farms espical")
    print(farms[0].get("name"))
    for x in farms:
        for key, value in x.items():
            print(key+": "+str(value))
main()



