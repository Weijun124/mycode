#!/usr/bin/env python3

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

def main():
    point=input("How many point you want to create\n ")
    if point.isdigit():
        t = np.linspace(0, 2 * np.pi*0.5, int(point))
            
        method_choose=input("Press 1 for cos curve, Press 2 for sin curve, Press others for other\n")
        if method_choose=="1":
            r = 0.5 + np.cos(t*2)
            x, y = r * np.cos(t), r * np.sin(t)
        elif method_choose=="2":
            r = 0.5 + np.sin(t*2) 
            x, y = r * np.cos(t), r * np.sin(t/2)
        else:
            r = 0.5 + np.sin(2*t)/np.cos(t)
            x, y = r * np.cos(t), r * np.sin(t/2)
        fig, ax = plt.subplots()
        ax.plot(x, y, "k")
        ax.set(aspect=1)
    else:
        print("please provide valid number")
    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    plt.savefig("/home/student/static/2018summaryv2.png")

main()
