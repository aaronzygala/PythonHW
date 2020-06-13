# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:55:00 2020

@author: Aaron
"""

lst_one = [x**2 for x in range(0,26)]
#print(lst_one)

lst_two = ["{}**2 = {}".format(x,x**2) for x in range(1,26)]
#print(lst_two)

lst_three = [(a,b,c) for b in range (1,101) for c in range(b,101) for a in range(c,101) if a**2 == b**2 + c**2]
#print(lst_three)

lst_four_input = ['eleven', 'seven', 'three', 'two', 'twenty', 'car']
lst_four = [(len(lst_four_input[i]), lst_four_input[i].upper()) for i in range(len(lst_four_input))
            if len(lst_four_input[i]) > 3]
#print(lst_four)

lst_five_input = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
lst_five = ["{}, {}".format(lastname, firstname) for (lastname, firstname) in 
            [(lst_five_input[i].split(" ")[1], lst_five_input[i].split(" ")[0]) for i in range(len(lst_five_input))]]
#print(lst_five)

def unzip(seq):
    first_list = []
    second_list = []
    
    for i in range(len(seq)):
        first_list.append(seq[i][0])
        second_list.append(seq[i][1])
    
    return_tuple = (first_list, second_list)
    return return_tuple

lst = [(1, "one"), (2, "two"), (3, "three")]
tup = unzip(lst)  
#print(tup) 
# prints ([1, 2, 3], ['one', 'two', 'three']) 

def concatenate(separator, *strings):
    final_string = ""
    for index, string in enumerate(strings):
        if index == (len(strings) - 1):
            final_string += string
        else:
            final_string += string + separator
    return final_string

#print(concatenate(' : ', 'one', 'two', 'three', 'four'))

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(lst[16:10:-1])

print(lst[16:10:-2])






