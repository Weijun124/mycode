#!/usr/bin/env python3
""" Alta3 Project | Weijun Huang
A script to convert a CSV file to a excel file by using pandas.
The "Toyota used car listing" was used for user to customize the information they want
and create their own excel based on this CSV file
Data website: https://www.kaggle.com/datasets/mysarahmadbhat/toyota-used-car-listing"""

import pandas as pd
import fontstyle as ft
import pyfiglet as pf
# Load the csv file and sorted by model' alphabet a=>z and create a python dictionary 
CSV=pd.read_csv("toyota_data.csv")
CSVSORT=CSV.sort_values('model',ignore_index=True)
DATAS=CSVSORT.to_dict(orient='records')
NEWLIST=[]

# Function for filter the model data
def model_choose():
    model_list=model_set(CSVSORT['model'])
    model_input=input(f"What type of model you are looking for? We have {model_list}\n ")
    for index, model in CSVSORT.copy(deep=False).iterrows():
        if model['model'].strip().lower()!=model_input.strip().lower():
            CSVSORT.drop(index, inplace=True)
        
        #         NEWLIST.append(model
        # pd.DataFrame(NEWLIST).to_excel("test1.xls", index=False)


def convert_to_excel():
    convert=input("Do you want to convert it to a excel file? [Y/n]")
    if(convert.lower()=='y'):
        pd.DataFrame(CSVSORT).to_excel("test.xlsx", index=False)
    else:
        print(CSVSORT)

# Function for filter the price level
def price_choose():
    min_price=input("Enter the least price you want\n")
    max_price=input("Enter the highest price you want\n")
    # Use list.copy() to avoid locate bug if you try to remove element from origional list
    for index, price in CSVSORT.copy(deep=False).iterrows():
        if price['price']<int(min_price) or price['price']>int(max_price):
            CSVSORT.drop(index, inplace=True)

    # for ele in NEWLIST.copy():
    #     if ele['price']<int(min_price) or ele['price']>int(max_price):
    #         NEWLIST.remove(ele)
    #     else:
    #         pass

def fuel_type_choose():
    fuel_type_list=fuel_type_set(CSVSORT['fuelType'])
    type_input=input(f"Based on the model and price you chose, we have {fuel_type_list} for you to choose\n ")
    for index, fuel in CSVSORT.copy(deep=False).iterrows():
        if fuel['fuelType'].strip().lower()!=type_input.strip().lower():
            CSVSORT.drop(index, inplace=True)
    print(CSVSORT)

# Function to create the model list
def model_set(model):
    type_list=[]
    for i in model:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list

def fuel_type_set(fueltype):
    fuel_list=[]
    for i in fueltype:
        if i not in fuel_list:
            fuel_list.append(i)
        else:
            pass
    return fuel_list



def main():
    print(ft.apply(pf.figlet_format("' Toyota used car listing ' for you to use", font = "slant" ), 'yellow'))
    user_opt=input("Press 'y' for checkout all the data in the list, Press other for specific search\n")
    if user_opt.lower()!='y':
        model_choose() 
        price_choose()
        fuel_type_choose()
    else:
        convert_to_excel()


if __name__ == "__main__":
    main()