#!/usr/bin/env python3
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use('Agg')
def main():
    excel_file='movies.xls'
    movies=pd.read_excel(excel_file)
    #print(movies.head())

    movies_sheet1=pd.read_excel(excel_file, sheet_name=0, index_col=0)
    movies_sheet2=pd.read_excel(excel_file, sheet_name=1, index_col=0)
    movies_sheet3=pd.read_excel(excel_file, sheet_name=2, index_col=0)

    #print(movies_sheet1)

    movies_sheet1.head(5).to_excel("5movies.xlsx")
    movies_sheet1.head(5).to_json("5movies.json")
    movies_sheet1.head(5).to_csv("5movies.csv")

    movies=pd.concat([movies_sheet1, movies_sheet2,movies_sheet3])
    #print(movies.shape)

    movies.drop_duplicates(inplace=True)
    print(movies.shape)

    sorted_by_gross=movies.sort_values(['Gross Earnings'], ascending=False)

    print(sorted_by_gross.head(10))

    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")

    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')

main()
