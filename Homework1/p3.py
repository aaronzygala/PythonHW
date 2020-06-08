# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:06:09 2020

@author: Aaron
"""

while True:
    try:
        dollar = input("Enter amount: ") #Get dollar amount and convert to float
        dollar = float(dollar)
        if dollar < 0: #If less than the value of a penny, input is invalid
            print("Invalid input.")
            break
        
        cents = dollar * 100 #Convert the dollar amount to the amount of cents
        
        quarters = cents / 25 #Perform calculation for quarters
        quarters = int(quarters)
        remainder = cents % 25
        
        dimes = remainder / 10 #Perform calculation for dimes
        dimes = int(dimes)
        remainder = remainder % 10
        
        pennies = remainder #Whatever is left is the penny amount
        pennies = int(pennies)
        
        total_coins = quarters + dimes + pennies #Find the total number of coins and the amount of dollars in coins
        total_coin_amount = quarters * 0.25 + dimes * 0.1 + pennies * 0.01 
        total_coin_amount = round(total_coin_amount, 2) #Round the float to 2 decimal places, to prevent floating point errors
        
        #Display the results
        print("${} makes {} quarters, {} dimes, and {} pennies ({} coins)."
              "Total amount in coins: ${}.".format(dollar, quarters, dimes, 
                                                   pennies, total_coins, total_coin_amount))
        
    except EOFError: #Infinite loop unless EOF is detected
        break
    
    