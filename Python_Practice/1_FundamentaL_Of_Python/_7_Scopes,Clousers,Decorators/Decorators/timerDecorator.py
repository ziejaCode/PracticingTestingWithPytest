

def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,args_str, elapsed))

        return result
    
    return inner


# recursive fibonacci
@timed
def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


#print(recursive_fib(6))

@timed
def fibRecursive(n):
    return recursive_fib(n)


# loop fibonnci 
@timed
def loop_fibonacci(n):
    fib1 = 1
    fib2 = 1
    for i in range(3, n+1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(loop_fibonacci(6))

from functools import reduce
# reduce fibo
@timed
def reduce_fibo(n):
    initial = (1,0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]

#print(reduce_fibo(6))


