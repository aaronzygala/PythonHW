# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:55:00 2020

@author: Aaron
"""

lst_one = [x**2 for x in range(0,26)]
print(lst_one)

lst_two = ["{}**2 = {}".format(x,x**2) for x in range(1,26)]
print(lst_two)

lst_three = []
print(lst_three)