""" Alta3 Project | Weijun Huang
    This is helping function file
    to execute the research and coverte file to xlsx """

import os
import sys
import time
import pandas as pd
import fontstyle as ft
import pyfiglet as pf

def model_choose(pandas_data):
    """ Function for filter the model data
        Could use df.loc for multiple model choose
        But got stuck when handle the error. In this
        case, user only can do single search """
    model_list=select_set(pandas_data['model'])
    model_input=input(f" What type of model you are looking for?\nWe have {model_list}\n>")
    print(ft.apply("\n Creating the table...", 'green_bg'))
    single_string_input(model_list,'model',model_input,pandas_data,model_choose)

def price_choose(pandas_data):
    """ Function for filter the price level """
    sentence=f" (Your current model price range is\n\
 between ${pandas_data['price'].min():,} and ${pandas_data['price'].max():,})"
    min_price=input(f"\n Enter the lowest price you want? {sentence}\n>")
    max_price=input(f"\n Enter the highest price you want? {sentence}\n>")
    range_number_input(min_price,max_price,'price',pandas_data,price_choose)

def transmission_type(pandas_data):
    """ Function for filter the transmission """
    transmission_list=select_set(pandas_data["transmission"])
    type_input=input(f"\n Based on your selection,\
 we have {transmission_list} for you to choose\n>")
    single_string_input(transmission_list,"transmission",type_input,pandas_data,transmission_type)

def mileage_choose(pandas_data):
    """ Function for filter
        the mileage range """
    sentence=f" (Your current mileage range is\n\
 between {pandas_data['mileage'].min():,} miles and {pandas_data['mileage'].max():,} miles)"
    min_mileage=input(f"\n Enter the minimum mileage you want? {sentence}\n>")
    max_mileage=input(f"\n Enter the maximum mileage you want? {sentence}\n>")
    range_number_input(min_mileage,max_mileage,'mileage',pandas_data,mileage_choose)

def fuel_type_choose(pandas_data):
    """ Function for filter the fuel type """
    fuel_type_list=select_set(pandas_data['fuelType'])
    type_input=input(f"\n Based on your selection, we have {fuel_type_list} for you to choose\n>")
    single_string_input(fuel_type_list,'fuelType',type_input,pandas_data,fuel_type_choose)

def convert_to_excel(pandas_data):
    """ Function to show the data or convert it
        to excel with xlsx form. Also can convert
        to json and csv in future need """
    os.system('clear')
    convert=input(" Do you want to convert it to a excel file? [Y/n]\n>")
    if convert.lower()=='y':
        print("\n Here is some example data you get\n\n",pandas_data.head(10))
        file_name=input("Please enter the name for the file\n>")
        try:
            print(ft.apply("\nCreating the Excel...", 'green_bg'))
            pd.DataFrame(pandas_data).to_excel(f"{file_name}.xlsx", index=False)
            end="File Is Created! Thanks For Using"
            print(ft.apply(pf.figlet_format(end, font = "digital" ), 'yellow'))
        except ValueError:
            print(ft.apply("\n Invalid input, Please try again\n", 'red_bg'))
            convert_to_excel(pandas_data)
    elif convert.lower()=='n':
        print(pandas_data)
        print(f'\n Result: Total {len(pandas_data.index)} vehicles meet your requirement')
        end="\nThanks For Using"
        print(ft.apply(pf.figlet_format(end, font = "digital" ), 'yellow'))
    else:
        convert_to_excel(pandas_data)

#Helping Function Area
def select_set(model):
    """ Function to create the selection list
        for model, fuel, and transmission type """
    type_list=[]
    for i in model:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list

def single_string_input(user_list,search_type,user_input,pandas_data,function_name):
    """ Helping function based on
        model, fuel and transmission
        input, and filter the result """
    # In the future, should use df.loc for filter the data, then turn this step
    # to go back for user to re-enter the last requirement
    if len(user_list)==0:
        print(ft.apply(" We don't have available car" \
            " based on your requirement, please try again",'red_bg'))
        sys.exit()
    user_search=False
    # Verify the user input is valid or not
    for name in user_list:
        if name.strip().lower()==user_input.strip().lower():
            user_search=True
    # Filter the data based on the user input
    if user_search:
        for index, data in pandas_data.copy(deep=False).iterrows():
            if data[search_type].strip().lower()!=user_input.strip().lower():
                pandas_data.drop(index, inplace=True)
    else:
        print(ft.apply("\n Invalid input. Please try again", 'red_bg'))
        time.sleep(1)
        os.system('clear')
        function_name(pandas_data)

def range_number_input(lowest_value,highest_value,search_type,pandas_data,function_name):
    """ Helping function based on
        input range (number), and
        filter the result """
    try:
        range_list=[int(lowest_value),int(highest_value)]
        range_list.sort() #in case user put min_price>max_price, auto fix this bug
        # Use df.copy() to avoid locate bug if you try to remove element from origional list
        if range_list[0]>=pandas_data[search_type].min() and \
            range_list[1]<=pandas_data[search_type].max():
            for index, data in pandas_data.copy(deep=False).iterrows():
                if data[search_type]<range_list[0] or data[search_type]>range_list[1]:
                    # Drop the value with current index data when price is not in the range
                    pandas_data.drop(index, inplace=True)
        else:
            print(ft.apply("\n Please enter "\
                 "the number within the range we provided \n"))
            function_name(pandas_data)
    except ValueError:
        print(ft.apply("\n Invalid input, Please try again", 'red_bg'))
        time.sleep(1)
        os.system('clear')
        function_name(pandas_data)
