# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:22:00 2024

@author: sahil
"""

"""
Given an array of integers, find the longest subarray where the absolute difference between 
any two elements is less than or equal to .


Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.


# Function Description: Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
Returns

int: the length of the longest subarray that meets the criterion


# Input Format

The first line contains a single integer , the size of the array .
The second line contains  space-separated integers, each an .

# Constraints
2<= n <= 100
0<= a[i] <=100
The answer >=2
"""


# Approach I
def pickingNumbers_1(a):
    """

    Parameters
    ----------
    a : INT ARRAY
        Consist of integers

    Returns
    -------
    Max(Max_length): INT        
                    Returning the max length of subarray which satisfies the condition

    """
    
    # Write your code here
    result=[]
    max_len = 1
    max_length =[]
    result.append(a[0])
    for i in range(1, len(a)):
        
        if all([abs(a[i] - x) <=1 for x in result]):
            result.append(a[i])
            max_len+=1
            print(a[i], "\n", result, "\n", max_len)
            print("\n\n")
            
        else:
            max_length.append(max_len)
            result.clear()
            result.append(a[i])
            max_len=1
            print(a[i], "\n", result, "\n", max_len, "\n")
    return max(max_length)
# The above failed as I thought this was a sliding window question but it's not.
# The above code works considering the subarray to be an sliding window but 
# there's no need to be so.
# Approach II
def pickingNumbers_2(a):
    """
    

    Parameters
    ----------
    a : INT ARRAY
        Same as above

    Returns
    -------
    INT
        Max length of the subarray.

    """
    # Write your code here
    result=[]
    max_length =[]

    a.sort()
    result.append(a[0])
    for i in range(1, len(a)):
        if all([abs(a[i]-x)<=1 for x in result]):
            result.append(a[i])
        else:
            max_length.append(len(result))
            result.clear()
            result.append(a[i])
    return max(max_length)
# In this code I sorted the array first and then added the first elemnet in the result array
# Next was to iterate through the other remaining elements and check if they satisfy the condition.
# This code failed one test case cause of a runtime error. I'm looking into it.   

"""
The fai;ed test case:
    100
66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 
66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 
66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 
66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 
66 66 66 66 66 66 66 66 66 66 66 66

So in this every elemnet of the given array satisfies the condition.

"""        
# Approach III
def pickingNumbers_3(a):
    # Write your code here
    result=[]
    max_length =[]
    a.sort()
    result.append(a[0])
    for i in range(1, len(a)):
        if all([abs(a[i]-x)<=1 for x in result]):
            result.append(a[i])
            # print(a[i], "\n", result)
        else:
            max_length.append(len(result))
            # print(a[i], "\n", max_length)
            result.clear()
            result.append(a[i])
            # print(result)
    max_length.append(len(result))  # this makes sure the 
                                    #len(result) is appended into the max_length
    return max(max_length)

"""
I learned about the 
1. all() function which will return logical AND of a list consisting of Boolean values.
2. List comprehension [(condition with variable_x) for x in array] --> we get a list of 
                                                                        Boolean values
"""
