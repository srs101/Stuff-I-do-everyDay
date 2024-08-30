# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:45 2024

@author: sahil
"""

# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    """
    
    """
    
    res=[]
    for x in player:
        r = ranked[:]
        r.append(x)
        ranks=[]
        s = set(r)
        s = list(s)
        s.sort(reverse=True)
        r.sort(reverse=True)
        rank=1
        for i in s:

            dup = r.count(i)
            if dup<=1:
                ranks.append(rank)
            else:
                ranks += [rank]*dup
            rank+=1
        res.append(ranks[r.index(x)])
    return res