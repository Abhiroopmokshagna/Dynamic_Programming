"""
Given a gold mine of n*m dimensions. 
Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner is at first column but can be at any row. 
He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right.
Find out maximum amount of gold he can collect.

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(2,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83

Create a 2-D matrix goldTable[][]) of the same as given matrix mat[][]. If we observe the question closely, we can notice following.

Amount of gold is positive, so we would like to cover maximum cells of maximum values under given constraints.
In every move, we move one step toward right side. So we always end up in last column. If we are at the last column, then we are unable to move right
If we are at the first row or last column, then we are unable to move right-up so just assign 0 otherwise assign the value of goldTable[row-1][col+1] to right_up. If we are at the last row or last column, then we are unable to move right down so just assign 0 otherwise assign the value of goldTable[row+1][col+1] to right up.
Now find the maximum of right, right_up, and right_down and then add it with that mat[row][col]. At last, find the maximum of all rows and first column and return it.

visit for more info: https://www.geeksforgeeks.org/gold-mine-problem/
"""

MAX = 100

def getMaxGold(gold, m, n):
    goldTable = [[0 for i in range(n)] for j in range(m)]
    for col in range(n-1,-1,-1):
        for row in range(m):
            if col == n-1:
                right = 0
            else:
                right = goldTable[row][col+1]
            
            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = goldTable[row-1][col+1]
            
            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = goldTable[row+1][col+1]
            
            goldTable[row][col] = gold[row][col]+max(right, right_up, right_down)
    res = goldTable[0][0]
    for i in range(1,m):
        res = max(res, goldTable[i][0])
    return res

gold = [[1,3,1,5],
        [2,2,4,1],
        [5,0,2,3],
        [0,6,1,2]]

m = 4
n = 4

print(getMaxGold(gold,m,n))