import pandas as pd

def main():
    ciscocsv = pd.read_csv("toyota_data.csv")
    ciscocsv.to_csv("converteddata.csv", index=False)
