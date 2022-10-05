#!/usr/bin/env python3
import pandas as pd

# Load the csv file and sorted by model' alphabet a=>z and create a python dictionary 
CSV=pd.read_csv("toyota_data.csv")
CSVSORT=CSV.sort_values('model')
DATAS=CSVSORT.to_dict(orient='records')


# Function for filter the model data
def model_choose(model_opt,model_list):
    new_list=[]
    if model_opt.lower()!='y':
        model_input=input(f"What type of model you are looking for? We have {model_list}\n ")
        for data in DATAS:
            if data['model'].strip().lower()==model_input.strip().lower():
                new_list.append(data)
        new_list=price_choose(new_list)
        print(new_list)
    else:
        print(CSVSORT)


# Function for filter the price level
def price_choose(new_list):
    min_price=input("Enter the least price you want\n")
    max_price=input("Enter the highest price you want\n")
    # Use list.copy() to avoid locate bug if you try to remove element from origional list
    for ele in new_list.copy():
        if ele['price']<int(min_price) or ele['price']>int(max_price):
            new_list.remove(ele)
        else:
            pass
    return new_list



# Function to create the model list
def model_set(CSVSORT):
    type_list=[]
    for i in CSVSORT:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list



def main():
    # Create unique list to show how many categories of toyota.csv has
    model_list=model_set(CSVSORT['model'])
    
    # Two options for user: 1-checkout all model 2-checkout specific model
    model_opt=input("Press 'y' for checkout all the data of Toyota'model, Press other for specific modal\n")
    # The answer will lead two different method to search
    model_choose(model_opt,model_list) 


main()
