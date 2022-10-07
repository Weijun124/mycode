#!/usr/bin/env python3
""" Alta3 Project | Weijun Huang
    A script to query the information from CSV data for user
    and convert it to a excel file by using pandas.
    The "Toyota used car listing" was used for user to customize the information they want
    and create their own excel based on this CSV file as Demo
    Data website: https://www.kaggle.com/datasets/mysarahmadbhat/toyota-used-car-listing """

import pandas as pd
import fontstyle as ft
import pyfiglet as pf
from function import model_choose
from function import price_choose
from function import transmission_type
from function import fuel_type_choose
from function import convert_to_excel

def start_run(csvsort):
    """Main Application Workflow start at this function"""
    print(ft.apply(pf.figlet_format("' Toyota used car listing ' "\
        "for you to use", font = "slant" ), 'yellow'))
    choose=" Press 'y' for checkout all the data in"\
         " the list. Press 'q' to retype the file name. Press other for specific search\n>"
    user_opt=input(choose)
    if user_opt.lower()=='y':
        convert_to_excel(csvsort)
    elif user_opt.lower()=='q':
        main()
    else:
        model_choose(csvsort)
        price_choose(csvsort)
        transmission_type(csvsort)
        fuel_type_choose(csvsort)
        convert_to_excel(csvsort)

def main():
    """ Load the csv file and sorted by model's alphabet order a=>z
        user can choose to check all the data or
        do the detail search based on their required """
    try:
        default = 'toyota_data.csv'
        file_name = input("Enter the file name you want to search"\
                    " (Press Enter for default file 'toyota_data.csv') \n>") or default
        data=pd.read_csv(file_name)
        csvsort=data.sort_values('model',ignore_index=True) # reorder the index after sort
        start_run(csvsort)
    except FileNotFoundError as error:
        print(f'{error}, please enter correct file name\n')
        main()
    except Exception as error: # If the file type or format are not correct
        print(f'{error}, please contact tpatrick@alta3.com\n')
        main()

if __name__ == "__main__":
    main()
