"""
Given a set of n elements, find number of ways of partitioning it.
Examples:

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. 


Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)

for example, S(4, 2) = 2*S(3, 2) + S(3, 1)

because if we need to make 4 elements into 2 partitions, 
we can add 4 to every set of the partitions of 3 elements into 2 sets

and if we want to keep 4 as separate partition,
we need to consider S(3, 1) because we can have {{4}, {1,2,3}} as a 2 set partition of 4 elements

another important part..
The total no of partitions possible with 4 elements will be S(4,1)+S(4,2)+S(4,3)+S(4,4)

How does above recursive formula work?
When we add a (n+1)’th element to k partitions, there are two possibilities.
1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
2) It is added to all sets of every partition, i.e., k*S(n, k)

for more, visit: https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
"""

N = int(input("Enter the Number of elements in the set: "))

partitions = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        if(i==j):
            partitions[i][j] = 1
            continue
        if(j==1):
            partitions[i][j] = 1
            continue
        partitions[i][j] = j*partitions[i-1][j] + partitions[i-1][j-1]

total_no_of_partitions = 0

for i in range(1,N+1):
    total_no_of_partitions += partitions[N][i]

print("The total no of partitions of a set with "+str(N)+" elements is: "+str(total_no_of_partitions))