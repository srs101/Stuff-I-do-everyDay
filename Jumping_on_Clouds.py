# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:43:03 2024

@author: sahil
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. The player can 
jump on any cumulus cloud having a number that is equal to the number of 
the current cloud plus  or . The player must avoid the thunderheads. 

Determine the minimum number of jumps it will take to jump from the starting 
postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are 
safe or  if they must be avoided.
"""

def jumpingOnClouds(c):
    # Write your code here
    """
    INPUT: Int Array
            Consisting of sequence of 1's and 0's. 
    RETURN: Int 
            Minimun number of jumps required to cross the sequence.
    
    """
    jmp = 0  # initializing the number of jumps
    i=0  # initiaalizing the pointer at 0 index of array
    n=len(c)
    while (i<n):
        if i+2 < n and c[i+2] == 0:  # checking if we can jump 2 places ahead
            jmp+=1
            i+=2
        elif i+1<n and c[i+1]==0:  # checking if we can jump on the next place
            jmp+=1
            i+=1
        else:
            break
    return jmp
# time complexity : O(n-3) -> Best case and O(n-2) -> most of the cases, where n is length of array
# space complexity: O(3) 
