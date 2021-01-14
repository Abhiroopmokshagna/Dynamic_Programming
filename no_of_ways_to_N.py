"""
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

for more understanding visit : https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
"""

def count_ways(n, table):
    if(n<0):
        return 0
    if(n==0 or n==1):
        return 1
    if(table[n] == None):
        table[n] = count_ways(n-1,table) + count_ways(n-3, table) +count_ways(n-5,table)
    return table[n]
table = [None] * 100
def main():
    n = 60
    print(count_ways(n,table))

if __name__ == '__main__':
    main()