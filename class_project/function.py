import re
import pandas as pd
import fontstyle as ft

def model_choose(csvsort):
    """Function for filter the model data"""
    model_list=select_set(csvsort['model'])
    model_input=input(f" What type of model you are looking for?\nWe have {model_list}\n>")
    print(ft.apply("\nCreating the table...\n", 'green_bg'))
    check_input(model_list,'model',model_input,csvsort)

def price_choose(csvsort):
    """Function for filter the price level"""
    min_price=input(" Enter the least price you want?\
        (Lowest price in your currentmodel is ${:,})\n>".format(csvsort['price'].min()))
    max_price=input(" Enter the highest price you want?\
        (Highest price in your current model is ${:,})\n>".format(csvsort['price'].max()))
    price_list=[min_price,max_price]
    try:
        # Using regex to verify valid input
        for i in price_list:
            re.match(r'\d+',i)
        # Use df.copy() to avoid locate bug if you try to remove element from origional list
        if int(min_price)>=csvsort['price'].min() and int(max_price)<=csvsort['price'].max():
            for index, price in csvsort.copy(deep=False).iterrows():
                if price['price']<int(min_price) or price['price']>int(max_price):
                    csvsort.drop(index, inplace=True)
        else:
            print(ft.apply("\n Price is out of the range. Please enter\
            the range between lowest and highest price we provided \n>"))
            price_choose(csvsort)
    except:
        print(ft.apply("\n Invalid input, Please try again\n", 'red-bg'))
        price_choose(csvsort)

def transmission_type(csvsort):
    """Function for filter the transmission"""
    transmission_list=select_set(csvsort["transmission"])
    type_input=input(f" Based on the model and price you chose,\
we have {transmission_list} for you to choose\n>")
    check_input(transmission_list,"transmission",type_input,csvsort)

def fuel_type_choose(csvsort):
    """Function for filter the fuel type"""
    fuel_type_list=select_set(csvsort['fuelType'])
    type_input=input(f" Based on the model, price and transmission\
you chose, we have {fuel_type_list} for you to choose\n>")
    check_input(fuel_type_list,'fuelType',type_input,csvsort)

def select_set(model):
    """Function to create the selection list for model type and fuel type"""
    type_list=[]
    for i in model:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list

def convert_to_excel(csvsort):
    """Function to show the data or convert it to excel with xlsx form"""
    convert=input(" Do you want to convert it to a excel file? [Y/n]\n>")
    if convert.lower()=='y':
        file_name=input("Please enter the name for the file\n>")
            
            # pd.DataFrame(csvsort).to_excel(f"{file_name}.xlsx", index=False)
            print(ft.apply("\n Invalid input, Please try again\n", 'red-bg'))
            convert_to_excel(csvsort)
    else:
        print(csvsort)

def check_input(user_list,search_type,user_input,csvsort):
    """Function to check the user input"""
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
        print(ft.apply("\n Invalid input. Please try again\n", 'red_bg'))
        model_choose(csvsort)