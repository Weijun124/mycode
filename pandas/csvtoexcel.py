#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - CSV to Excel"""

import pandas

def main():
    df=pandas.read_csv("5movies.csv")
    df.to_excel("5movies-translated-from-json.xlsx")

if __name__=="__main__":
    main
