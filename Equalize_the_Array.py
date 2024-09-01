# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:30:33 2024

@author: sahil

Given an array of integers, determine the minimum number of elements to delete 
to leave only elements of equal value.


# Function Description
Complete the equalizeArray function in the editor below.
equalizeArray has the following parameter(s):
int arr[n]: an array of integers

# Returns
int: the minimum number of deletions required

# Input Format
The first line contains an integer , the number of elements in .
The next line contains  space-separated integers .
"""

def equalizeArray(arr):
    # Write your code here
    """
    INPUT: Int Array
            Arrays consisting of Integers
    RETURN: Int
            Minimun numbers of elements to be deleted to equalize the array
    """
    return abs(max([arr.count(element) for element in set(arr)]) - len(arr))

# pretty straight forward question, LOGIC: we find the element with most occurence
# and after finding it, we subtract its occurences with the length of array.
"""
EXPLAINATION OF ABOVE CODE 
I made use of list comprehension, max(), set() list.count() and abs()
Firstly i converted the array to a set, then iterate throught it to get count of every element in the
array. After that I get the count which is the maximun using max() and subtract this result with
length of array i.e len(arr). I put this results under abs() just to be safe and not ot return any 
negative values.

In simpler terms my code would be as (aka Brute Force Approach):
    
    temp = set(arr)  # remove duplicates from arr
    occurence =[]    # initialize empty list to store occurences 
    for element in temp:
        occurence.append(arr.count(element))   # adding count(element) in occurence
    max_occurence = max(occurence)             # getting the maximum occurnces
    return abs(max_occurence - len(arr))      # subtracting and returning the absolute value

"""