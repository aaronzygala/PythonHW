# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:46:04 2020

@author: Aaron
"""

'''
A function that takes a string as parameter 
and returns a new string that is the same as the 
parameter without any vowels ('a'', 'e', 'i', 'o', 'u'). 
'''
def no_vowels(string_with_vowels):
    string_without_vowels = string_with_vowels
    #Array containing lowercase and uppercase vowels
    vowel_array = ['a','e','i','o','u','A','E','I','O','U']
    
    #Iterate through each character in the string, and if the character
    #is a vowel, then remove it
    for character in string_without_vowels:
        if(character in vowel_array):
            string_without_vowels = string_without_vowels.replace(character,'')
    return string_without_vowels
            


'''
A function that takes as parameter a string s and an 
integer n and that returns a substring of s of length n that is duplicated 
with no overlap in s. If no such string exists then the function should 
return "" (the empty string).
'''
def find_dup(s, n):
    #Default the duplicate value to empty string
    duplicate = ""

    for i in range(len(s)):
        #The current substring starts at the index and has a length of n
        sub_str = s[i:i+n]
        #Check if the substring exists later in the string(starting at the end of the
        #current substring). If it does, return the duplicate.
        if(s.find(sub_str, i+n) != -1):
            duplicate = sub_str
            
    return duplicate


#Main function to test the functions
def main():
    #Test no_vowels
    print(no_vowels("Python rules!")) #Returns Pythn rls!
    print(no_vowels("")) #Returns nothing
    print(no_vowels("AEIOU")) #Returns nothing(all vowels)
    print(no_vowels("BCDFG")) #Returns BCDFG
    print(no_vowels("Aaron Zygala")) #Returns rn Zygl
    
    #Test find_dup
    print(find_dup("abcdefcdegh", 3)) #Returns cde
    print(find_dup("abcdefgh", 3)) #Returns nothing(no repeats)
    print(find_dup("abcabcabcabc", 3)) #Returns abc
    print(find_dup("AEAOU", 1)) #Returns A
    print(find_dup("CarBatDogCarHat", 3)) #Returns Car
        
main()
