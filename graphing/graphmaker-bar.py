#!/usr/bin/env python3

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
def main():
    N = 400
    t = np.linspace(0, 2 * np.pi, N)
    r = 0.5 + np.cos(t)
    x, y = r * np.cos(t), r * np.sin(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, "k")
    ax.set(aspect=1)
    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    plt.savefig("/home/student/static/2018summaryv2.png")

main()
