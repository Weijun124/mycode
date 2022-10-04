#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    url="https://api.magicthegathering.io"
    # create resp, which is our request object
    resp = requests.get(f"{url}/v1/sets")
    #print(type(resp))
    #print(dir(resp))
    #print(resp.json().keys())
    cardsets=resp.json().get("sets")
    with open ("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets:
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)




main()
