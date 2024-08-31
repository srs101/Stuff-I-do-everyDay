# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:11:51 2024

@author: sahil

SEQUENCE EQUATION

Given a sequence of  integers,  where each element is distinct and satisfies . 
For each  where , that is  increments from  to , find any integer  such that  
and keep a history of the values of  in a return array.

Example


Function Description

Complete the permutationEquation function in the editor below.

permutationEquation has the following parameter(s):

int p[n]: an array of integers
Returns

int[n]: the values of  for all  in the arithmetic sequence  to 
"""

def permutationEquation(p):
    # Write your code here
    res=[]
    for x in range(1, len(p)+1):
        i=p.index(x)
        i=p.index(i+1)  
        res.append(i+1)
        
    return res
        
# Took a few minutes to get the question
# pretty staightforward. 
"""
consider example:
    n = 3
    arr = 2,3,1
    
    soln:
        p[1] = 2, p[2] = 3, p[3] = 1
        
        for x in range (1,4):
            # at x = 1
            p[3] = 1
            p[2] = 3
            => p[p[2]] = p[3] = 1
            
            so, i = index of 1 in arr (2, as arrays are indexed from 0)
            i+1 = 3...we got p[3]
            now 3 is at index 1 but we add one to get p[2]
            we append 2 in the result.
            
"""