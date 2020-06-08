# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:37:50 2020

@author: Aaron
"""
import matplotlib.pyplot as plt

"""
A program p3.py that reads in a string fun_str from the terminal a mathematical 
function definition that uses symbol x as a parameter, a domain (float [xmin,xmax] interval), 
and the number of samples ns (an integer), and then: 
"""

#Define the variables used by the program
fun_str = input("Enter function with variable x: ")
ns_str = input("Enter number of samples: ")
ns_int = int(ns_str)
xmin_str = input("Enter xmin: ")
xmin_flt = int(xmin_str)
xmax_str = input("Enter xmax: ")
xmax_flt = int(xmax_str)

#The domain and range of the graph
xs=[]
ys=[]

dx = (xmax_flt-xmin_flt)/ns_int #delta between points

#Calculate the values of xs using dx
x = xmin_flt
while x <= xmax_flt:  
    xs.append(x)
    x+=dx
#Calculate the values of y from the function   
for x in xs:
  y = eval(fun_str)
  ys.append(y)

#Print the table to the console
print("\n     x       y\n" +
      "--------------------")
for i in range(ns_int + 1):
    print("{:8.4f} {:8.4f}".format(xs[i], ys[i])) #Format the string to display a neat table

#Display the graph with labeled titles
plt.title(fun_str)
plt.xlabel("xs - Domain")
plt.ylabel("ys - Range")
plt.plot(xs,ys, 'b.-') #plot dots and lines
plt.show() #display plot