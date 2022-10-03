#!/usr/bin/env python3
import pandas as pd

def main():
    csv=pd.read_csv("data.csv")
    print(csv['model'])
main()
