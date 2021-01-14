def fibonacci(n, lookup):
    if(lookup[n] == None):
        lookup[n] = fibonacci(n-1,lookup) + fibonacci(n-2, lookup)
    return lookup[n]

lookup = [None] * 101

lookup[0] = 0

lookup[1] = 1

def main():
    print(fibonacci(16, lookup))

if __name__ == '__main__':
    main()