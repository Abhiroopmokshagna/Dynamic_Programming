"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

for more, visit https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
"""

def subsetSum(set, sum, n):
    subsetdp = [[False for i in range(sum+1)] for i in range(n+1)]
    for i in range(n+1):
        subsetdp[i][0] = True
    for i in range(1, sum+1):
        subsetdp[0][i] = False
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if(set[i-1] > j):
                subsetdp[i][j] = subsetdp[i-1][j]
            else:
                subsetdp[i][j] = subsetdp[i-1][j] or subsetdp[i-1][j-set[i-1]]
    return subsetdp[n][sum]

set = [2,3,5,10,20]
n = len(set)
print(subsetSum(set, 32, n))
