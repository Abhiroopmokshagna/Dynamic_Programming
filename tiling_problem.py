"""
Given a “2 x n” board and tiles of size “2 x 1”, 
count the number of ways to tile the given board using the 2 x 1 tiles. 
A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

Example 1:

Input: n = 4

Output: 3

Explanation:
For a 2 x 4 board, there are 3 ways

All 4 vertical
All 4 horizontal
2 vertical and 2 horizontal

Example 2:

Input: n = 3

Output: 2

Explanation:

We need 2 tiles to tile the board of size  2 x 3.

We can tile the board using following ways

Place all 3 tiles vertically.
Place 1 tile vertically and remaining 2 tiles horizontally.

"""
tiling_ways = {}
tiling_ways[1] = 1
def count_tiling_ways(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    if n in tiling_ways.keys():
        return tiling_ways[n]
    tiling_ways[n] = count_tiling_ways(n-1) + count_tiling_ways(n-2)
    return tiling_ways[n]

n = int(input("Enter the length of board: "))
print("The number of ways of tiling the board: "+str(count_tiling_ways(n)))
   