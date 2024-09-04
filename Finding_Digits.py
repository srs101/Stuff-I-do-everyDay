# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:29:11 2024

@author: sahil
An integer d is a divisor of an integer n if the remainder of n/d=0.
Given an integer, for each digit that makes up the integer 
determine whether it is a divisor. Count the number of divisors 
occurring within the integer.
"""
def findDigits(n):
    """
    

    Parameters
    ----------
    n : INTEGER
        An integer number

    Returns
    -------
    INTEGER
        Count of numbers of digits of the given integer n
        are its divisor.

    """
    # Write your code here
    div = [int(x) for x in str(n)]  # converting to individual digits
    res = [n % x for x in div if x!=0]
    return res.count(0)
"""
Firstly, I convetred the given integer to a string using str(),
then using a loop to interate over every character and converting it 
to an integer while making use of list comprehension and store this as 
new list "div"
Then again using list comprehension and loop to iterate over element of div,
dividing it by the given n while making sure not dividing 0 by n and storing 
the remainder of this in list "res" and finally returing the occurences of 0
in res by using list.count().

Brute force Approach:
    digits = []  # list to store individual digits
    remainders=[]  # list to store remainders
    str_n = str(n)  # converting given integer to string
    for i in str_n:
        x = int(i)  # converting char to int
        digits.append(x)  # storing individual digit
    for i in digits:
        if i!=0:
            remainders.append(n % i)  # storing remainders 
    return remainders.count(0)  # returning the count of 0s in remainders[]
            
        
"""