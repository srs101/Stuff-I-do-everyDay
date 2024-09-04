# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:00:25 2024

@author: sahil

# Function Description
Complete the extraLongFactorials function in the editor below. 
It should print the result and return.

extraLongFactorials has the following parameter(s):
n: an integer
"""

def extraLongFactorials(n):
    """
    INPUT: INTEGER
            Find the factorial of given integer
    """
    # Write your code here
    res = 1
    for i in range(1, n+1):
        res*=i
    print(res)