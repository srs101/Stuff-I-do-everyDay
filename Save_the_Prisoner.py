# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:12:55 2024

@author: sahil

Q: Save The Prisioner
A jail has a number of prisoners and a number of treats to pass out to them. 
Their jailer decides the fairest way to divide the treats is to seat the prisoners 
around a circular table in sequentially numbered chairs. A chair number will be drawn 
from a hat. Beginning with the prisoner in that chair, one candy will be handed to each 
prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, 
but it tastes awful. Determine the chair number occupied by the prisoner who will receive that 
candy.

# Function Description
Complete the saveThePrisoner function in the editor below. 
It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

int n: the number of prisoners
int m: the number of sweets
int s: the chair number to begin passing out sweets from

# Returns
int: the chair number of the prisoner to warn
"""

def saveThePrisoner(n, m, s):
    # Write your code here
    """
    
    """
    # no. of prisoner = n
    # no. of sweets = m
    # starting pos = s

    rem = m % n  # no. of sweets remaining after x complete rounds od distribution
    print(rem)
    end = s + rem - 1 # as the starting prisoner got a candy
    print(end)
    if end > n:
        end = end - n
        print("if cond. ", end)
    return end
# failed 7 test cases

