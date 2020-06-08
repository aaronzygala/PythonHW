# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:30:20 2020

@author: Aaron
"""


"""
Write a function called line_number that takes as parameters two strings representing
 file names. Assume these are text files, like .py source files. The function reads the 
 file indicated by the first parameter and writes its lines prefixed by the line number 
 to a new file named after the second parameter.

The function must have a proper docstring and annotations. Use try/except and
 in case of an error print a user-friendly message to the terminal and re-raise 
 the exception.
"""

def line_number(input_filename, output_filename):
    input_file = open(input_filename, "r")
    output_file = open(output_filename, "w")
    
    i = 1
    for line_str in input_file:
        new_str = ""
        line_str = line_str.strip()
        new_str = str(i) + " " + line_str
        print(new_str, file=output_file)
        i+=1
        
    input_file.close()
    output_file.close()
    
#main 
#line_number("p1.py", "p1.py.txt")   

"""
Write a function called strip_comments that takes as parameters a source file name 
(string, e.g. a Python file), a destination file name (string), and a comment prefix
 (string) and that removes all comments that start with the prefix string from the first 
 source file and writes the resulting content to the second file whose name is given. 
 
 For Python, the prefix is "#", for C/C++ it could be "//". If a comment starts at the 
 beginning of a line then the entire line is removed from the resulting file. A comment 
 in Python and many other languages continues from the prefix string to the end f the line.
"""

def strip_comments(input_filename, output_filename, comment_prefix):
    input_file = open(input_filename, "r") #COMMMENT
    output_file = open(output_filename, "w")  #COMMMENT
#COMMMENT
    for line_str in input_file: #COMMMENT
        line_str = line_str.strip() #COMMMENT
        new_str = line_str #COMMMENT
        for index, char in enumerate(line_str): #COMMMENT
            if char == comment_prefix:
                new_str = line_str[0:index]
                
        print(new_str, file=output_file)
        
    input_file.close()
    output_file.close()
strip_comments("p1.py", "p1.py.txt", "#")






