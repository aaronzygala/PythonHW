# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:27:53 2020

@author: Aaron
"""
import math
import matplotlib.pyplot as pyplot

# Main infinite loop
while True:
    # Get the inputs of a, b, and c
    a = input("Enter a: ")
    a = float(a)
    if(a == 0): # If a is 0, exit the infinite loop 
        print("Good bye.")
        break
    b = input("Enter b: ")
    b = float(b)
    
    c = input("Enter c: ")
    c = float(c)
    
    discriminant = (b**2) - (4 * a * c) #Calculate the discriminant of the quadratic formula
    # Use the discriminant to determine the number of solutions, and print the solutions
    if(discriminant < 0):
        print("No real solutions")
    elif(discriminant == 0):
        print("One solution")
        x = ((-b) + math.sqrt(discriminant))/(2*a)
        print("x = " + str(x))
    else:
        print("Two solutions")
        x1 = ((-b) + math.sqrt(discriminant))/(2*a)
        x2 = ((-b) - math.sqrt(discriminant))/(2*a)
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    
    xs=[]
    ys=[]
    
    x0 = -5 #lower bound
    x1 = 5 #upper bound
    n = 100 #number of points
    dx = (x1-x0)/n #delta between points
    
    x = x0
    while x <= x1: #for 100 values between x0 and x1
        y=a*x**2+b*x+c #calculate the y values 
        
        xs.append(x) #append to each list
        ys.append(y)
        x+=dx
    
    pyplot.plot(xs,ys, 'b.-') #plot dots and lines
    pyplot.show() #display plot
    
            
