#!/usr/bin/env python3
import csv

csvtoyota=open("toyota.csv","a")
with open('toyota_cars.csv',mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row, file=csvtoyota)
