#!/usr/bin/env python3
""" Alta3 Project | Weijun Huang
A script to query the information from CSV data for user
and convert it to a excel file by using pandas.
The "Toyota used car listing" was used for user to customize the information they want
and create their own excel based on this CSV file
Data website: https://www.kaggle.com/datasets/mysarahmadbhat/toyota-used-car-listing"""

import pandas as pd
import fontstyle as ft
import pyfiglet as pf
from function import model_choose
from function import price_choose
from function import transmission_type
from function import fuel_type_choose
from function import convert_to_excel

def main():
    """Load the csv file and sorted by model's alphabet a=>z
    user can choose to check all the data or
    do the detail search by putting condition """
    data=pd.read_csv("toyota_data.csv")
    csvsort=data.sort_values('model',ignore_index=True)
    start="' Toyota used car listing ' for you to use"
    print(ft.apply(pf.figlet_format(start, font = "slant" ), 'yellow'))
    choose=" Press 'y' for checkout all the data in the list, Press other for specific search\n>"
    user_opt=input(choose)
    if user_opt.lower()!='y':
        model_choose(csvsort)
        price_choose(csvsort)
        transmission_type(csvsort)
        fuel_type_choose(csvsort)
        convert_to_excel(csvsort)
    else:
        convert_to_excel(csvsort)

if __name__ == "__main__":
    main()
