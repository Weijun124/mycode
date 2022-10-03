#!/usr/bin/env python3
import pandas as pd

def model_choose(user_opt,model_opt):
    if user_opt.lower()!='y':
        model=input(f"What type of model you are looking for? We have {model_opt} ")
        print(csv[model])



def main():
    csv=pd.read_csv("toyota_data.csv")
    csv_sort=csv.sort_values('model')
    print(csv_sort['model'])
    list_model=set(csv_sort['model'])
    data_choose=input('Press \'y\' for all the modal of the Toyota, Press other for specific modal')
    model_choose(data_choose,list_model) 


main()
