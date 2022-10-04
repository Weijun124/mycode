#!/usr/bin/env python3
import pandas as pd

# Load the csv file and sorted by model' alphabet a=>z 
csv=pd.read_csv("toyota_data.csv")
csv_sort=csv.sort_values('model')
newlist=[]
# Function for filter the model data
def model_choose(model_opt,model_list):
    if model_opt.lower()!='y':
        model_input=input(f"What type of model you are looking for? We have {model_list}\n ")
        for index, row in csv_sort.iterrows():
            if row['model'].strip().lower()==model_input.strip().lower():
                newlist.append(row)
        print(newlist)
        
    else:
        print(csv_sort)

# Function for filter the price level
def price_choose(row):
    min_price,max_prince=input("Enter the price range between 1,000 and 50,000").split()
    print(min_price,max_price)






# Function to create the model list
def model_set(csv_sort):
    type_list=[]
    for i in csv_sort:
        if i not in type_list:
            type_list.append(i)
        else:
            pass
    return type_list



def main():
    # Create unique list to show how many categories of toyota.csv has
    model_list=model_set(csv_sort['model'])
    
    # Two options for user: 1-checkout all model 2-checkout specific model
    model_opt=input("Press 'y' for checkout all the data of Toyota'model, Press other for specific modal\n")
    # The answer will lead two different method to search
    model_choose(model_opt,model_list) 


main()
