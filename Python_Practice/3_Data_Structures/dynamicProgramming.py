'''
Created on 21 Dec 2019
@author: M.Laptop
'''

def fibonacci(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = 1
        print(lookup)
    if lookup[n] is None:
        lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup)
        print(lookup)
    return lookup[n]

if __name__ == "__main__":
    n = 5
    lookup = [None]*(n+1)
    print(lookup)
    print("Fibonacci using DP {}".format(fibonacci(n, lookup)))



def fibonacci1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)


print("Fibonacci using recursion: {}".format(fibonacci1(5)))


'''  '''

def fibonacci2(n):    
    if n == 0 or n == 1:
        return 1
    else:
        f = [1, 1]
        for i in range(1,n):
            f.append(f[i] + f[i-1])            
        return f
           
print(fibonacci2(7))
