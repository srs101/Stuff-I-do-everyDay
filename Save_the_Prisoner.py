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
    INPUT: Int n, Int m, Int s
            n - Number of total Prisoners
            m - Total number of candies
            s - Starting position of distribution
    RETURN: Int pos
            Position of prisoner who get's the last candy
    """
    
    
    if (s + m - 1) % n != 0:
        return (s + m - 1) % n
    else:
        return n
    """
    
    pos = 0
    for i in range(m):
        pos = (s + i) % n
    if pos != 0:
        return pos
    else:
        return n
        
    """

