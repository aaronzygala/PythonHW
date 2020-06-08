# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:16:54 2020

@author: Aaron
"""


"""
A program that reads from the terminal a positive integer n 
and that computes and displays to the terminal all possible Pythagorean triples (a,b,c), 
where 0 < a,b,c <= n.
"""

def pythagorean_triples():
    print("This is a program that reads a value of n from the\n" +
          "terminal and displays all possible Pythagorean triples\n" +
          "(a,b,c) where 0 < a,b,c <= n")
    
    n_str = input("Please enter the value of n: ")
    n_int = int(n_str)
    #Only accept positive values a n
    if(n_int < 0):
        print("Error! n must be a positive integer")
        return
    
    #Iterate over each value in the equation (a, b and c) and perform the
    #calculation to check
    print("\nPythagorean triplets less than n (inclusive):")
    for a in range(1, n_int + 1):
        for b in range(a + 1, n_int + 1):
            for c in range (b + 1, n_int + 1):
                #If a triplet is found, display the values
                if (a**2 + b**2) == c**2:
                    print("a = {}, b = {}, c = {}".format(a,b,c))
                    
#Call to the function
pythagorean_triples()


