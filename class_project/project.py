#!/usr/bin/env python3
""" Alta3 Project | Weijun Huang
A script to query the information from CSV data for user and convert it to a excel file by using pandas.
The "Toyota used car listing" was used for user to customize the information they want
and create their own excel based on this CSV file
Data website: https://www.kaggle.com/datasets/mysarahmadbhat/toyota-used-car-listing"""

import pandas as pd
import fontstyle as ft
import pyfiglet as pf
import re

# Function for filter the model data
def model_choose(CSVSORT):
    model_list=select_set(CSVSORT['model'])
    model_input=input(f" What type of model you are looking for?\nWe have {model_list}\n>")
    print(ft.apply("\nCreating the table...\n", 'green_bg'))
    model_search=False
    # Verify the user input is valid or not
    for name in model_list:
        if name.strip().lower()==model_input.strip().lower():
            model_search=True
    # Filter the data based on the user input
    if model_search:
        for index, model in CSVSORT.copy(deep=False).iterrows():
            if model['model'].strip().lower()!=model_input.strip().lower():
                CSVSORT.drop(index, inplace=True)
    else:
        print(ft.apply("\n Invalid input. Please try again\n", 'red_bg'))
        model_choose(CSVSORT)       

# Function for filter the price level
def price_choose(CSVSORT):
    min_price=input(" Enter the least price you want? (Lowest price in your current model is ${:,})\n>".format(CSVSORT['price'].min()))
    max_price=input(" Enter the highest price you want? (Highest price in your current model is ${:,})\n>".format(CSVSORT['price'].max()))
    price_list=[min_price,max_price]
    try:
        # Using regex to verify valid input
        for i in price_list:                
            re.match(r'\d+',i)
        # Use list.copy() to avoid locate bug if you try to remove element from origional list
        if int(min_price)>=CSVSORT['price'].min() and int(max_price)<=CSVSORT['price'].max():
            for index, price in CSVSORT.copy(deep=False).iterrows():
                if price['price']<int(min_price) or price['price']>int(max_price):                         
                    CSVSORT.drop(index, inplace=True)
        else:
            print(ft.apply("\n Price is out of the range. Please enter the range between lowest and highest price we provided \n>"))
            price_choose(CSVSORT)
    except:
        print(ft.apply("\n Invalid input, Please try again\n", 'red-bg'))
        price_choose(CSVSORT)

def fuel_type_choose(CSVSORT):
    fuel_type_list=select_set(CSVSORT['fuelType'])
    type_input=input(f" Based on the model and price you chose, we have {fuel_type_list} for you to choose\n>")
    for fuel in fuel_type_list:
        if type_input.strip().lower()==fuel.strip().lower():
            pass
        else:
            print(ft.apply("\n Invalid input, Please try again\n", 'red-bg'))
            fuel_type_choose(CSVSORT)
    for index, fuel in CSVSORT.copy(deep=False).iterrows():
        if fuel['fuelType'].strip().lower()!=type_input.strip().lower():
            CSVSORT.drop(index, inplace=True)



# Function to create the selection list for model type and fuel type
def select_set(model):
    type_list=[]
    for i in model:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list

# Function to show the data or convert it to excel with xlsx form
def convert_to_excel(CSVSORT):
    convert=input(" Do you want to convert it to a excel file? [Y/n]\n>")
    if(convert.lower()=='y'):
        pd.DataFrame(CSVSORT).to_excel("test.xlsx", index=False)
    else:
        print(CSVSORT)

def main():
     # Load the csv file and sorted by model' alphabet a=>z 
    CSV=pd.read_csv("toyota_data.csv")
    CSVSORT=CSV.sort_values('model',ignore_index=True)
    print(ft.apply(pf.figlet_format("' Toyota used car listing ' for you to use", font = "slant" ), 'yellow'))
    user_opt=input(" Press 'y' for checkout all the data in the list, Press other for specific search\n>")
    if user_opt.lower()!='y':
        model_choose(CSVSORT) 
        price_choose(CSVSORT)
        fuel_type_choose(CSVSORT)
        convert_to_excel(CSVSORT)
    else:
        convert_to_excel(CSVSORT)

if __name__ == "__main__":
    main()