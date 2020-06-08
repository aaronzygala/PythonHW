# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:04:09 2020

@author: Aaron
"""


# Giving the instructions to the user
print("This program determines the weekly salary for an employee.\n" +
      "The salary is the sum of the hourly rate times the hours worked, plus the bonus. \n" +
      "For work hours exceeding 40 per week, an overtime rate of 1.5 is applied. \n" +
      "The user must indicate if the worker has received a bonus by answering a y/n question.\n" +
      "Input consists of: hours worked, hourly rate, bonus. \n" +
      "The output is the total salary for this week.")

# Defining the initial input variables
rate_per_hour = input("Enter the hourly salary: ")
rate_per_hour = float(rate_per_hour)
hours_worked = input("Enter the number of hours worked in a week: ")
hours_worked = float(hours_worked)
yes_no = input("Has the worker received a bonus (y/n): ")

bonus = 0 # Defaulting bonus to 0
if(yes_no == 'y'):
    bonus = input("Enter the bonus: ")
    bonus = float(bonus)

overtime_pay = 0 # Defaulting overtimePay to 0
if(hours_worked > 40):
    overtime_pay = (hours_worked - 40) * rate_per_hour * 1.5
    non_overtime_pay = 40 * rate_per_hour
else:
    non_overtime_pay = hours_worked * rate_per_hour

# Performing the calculation with all of the values
total_salary = overtime_pay + non_overtime_pay + bonus

# Printing the result to the user
print("The total salary is: ${} (overtime pay ${})".format(total_salary,overtime_pay))













