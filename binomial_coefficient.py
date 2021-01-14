"""
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).
"""
def binomialcoefficient(n,r):
    if(n-r<r):
        r = n-r
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res / (i+1)
    return res

n = int(input())
r = int(input())

res = binomialcoefficient(n,r)

print(res)