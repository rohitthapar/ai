#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Sun Mar 20 16:48:17 2022

@author: riddhiarora
"""


def riddhi_Manhattan(s, g):
    total_m = 0
    for i in range(3):
        for j in range(3):
            temp = s[i][j]
            if temp != 0:
                x1 = i
                y1 = j
                for i1 in range(3):
                    for j1 in range(3):
                        if g[i1][j1] == temp:
                            x2 = i1
                            y2 = j1
                            total_m += ((abs(x1 - x2)) + (abs(y1 - y2)))
    return total_m


def main():
    s = [[2, 0, 3], [1, 8, 4], [7, 1, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 1, 5]]
    man = riddhi_Manhattan(s, g)
    print("Manhattan:", man)


if _name == "main_":
    main()