""" Alta3 Project | Weijun Huang
    This is helping function file
    to execute the research and coverte file to xlsx """

import pandas as pd
import fontstyle as ft
import pyfiglet as pf

def model_choose(csvsort):
    """Function for filter the model data
        Could use df.loc for multiple model choose
        But got stuck when handle the error. In this
        case, user only can do single search"""
    model_list=select_set(csvsort['model'])
    model_input=input(f" What type of model you are looking for?\nWe have {model_list}\n>")
    print(ft.apply("\nCreating the table...", 'green_bg'))
    check_input(model_list,'model',model_input,csvsort,model_choose)

def price_choose(csvsort):
    """Function for filter the price level"""
    sentence=f" (Your current model price range is\n\
 between ${csvsort['price'].min():,} and ${csvsort['price'].max():,})"
    min_price=input(f" Enter the least price you want? {sentence}\n>")
    max_price=input(f" Enter the highest price you want? {sentence}\n>")
    try:
        price_list=[int(min_price),int(max_price)]
        price_list.sort() #in case user put min_price>max_price, auto fix this bug
        # Use df.copy() to avoid locate bug if you try to remove element from origional list
        if price_list[0]>=csvsort['price'].min() and price_list[1]<=csvsort['price'].max():
            for index, price in csvsort.copy(deep=False).iterrows():
                if price['price']<price_list[0] or price['price']>price_list[1]:
                    # Drop the value with current index data when price is not in the range
                    csvsort.drop(index, inplace=True)
        else:
            print(ft.apply("\n Please enter "\
                 "the price within the range we provided \n"))
            price_choose(csvsort)
    except ValueError:
        print(ft.apply("\n Invalid input, Please try again", 'red_bg'))
        price_choose(csvsort)

def transmission_type(csvsort):
    """Function for filter the transmission"""
    transmission_list=select_set(csvsort["transmission"])
    type_input=input(f" Based on your selection, we have {transmission_list} for you to choose\n>")
    check_input(transmission_list,"transmission",type_input,csvsort,transmission_type)

def fuel_type_choose(csvsort):
    """Function for filter the fuel type"""
    fuel_type_list=select_set(csvsort['fuelType'])
    type_input=input(f" Based on your selection, we have {fuel_type_list} for you to choose\n>")
    check_input(fuel_type_list,'fuelType',type_input,csvsort,fuel_type_choose)

def select_set(model):
    """Function to create the selection list for model, fuel, and transmission type"""
    type_list=[]
    for i in model:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list

def check_input(user_list,search_type,user_input,csvsort,function_name):
    """ Helping function based on
        model, fuel and transmission
        input, and filter the result """
    user_search=False
    # Verify the user input is valid or not
    for name in user_list:
        if name.strip().lower()==user_input.strip().lower():
            user_search=True
    # Filter the data based on the user input
    if user_search:
        for index, data in csvsort.copy(deep=False).iterrows():
            if data[search_type].strip().lower()!=user_input.strip().lower():
                csvsort.drop(index, inplace=True)
    else:
        print(ft.apply("\n Invalid input. Please try again", 'red_bg'))
        function_name(csvsort)

def convert_to_excel(csvsort):
    """Function to show the data or convert it to excel with xlsx form"""
    convert=input(" Do you want to convert it to a excel file? [Y/n]\n>")
    if convert.lower()=='y':
        file_name=input("Please enter the name for the file\n>")
        try:
            print(ft.apply("\nCreating the Excel...", 'green_bg'))
            pd.DataFrame(csvsort).to_excel(f"{file_name}.xlsx", index=False)
            end="File Is Created! Thanks For Using"
            print(ft.apply(pf.figlet_format(end, font = "digital" ), 'yellow'))
        except ValueError:
            print(ft.apply("\n Invalid input, Please try again\n", 'red_bg'))
            convert_to_excel(csvsort)
    elif convert.lower()=='n':
        print(csvsort)
        print(f' Result: Total {len(csvsort.index)} vehicles meet your requirement')
        end="Thanks For Using"
        print(ft.apply(pf.figlet_format(end, font = "digital" ), 'yellow'))
    else:
        convert_to_excel(csvsort)
