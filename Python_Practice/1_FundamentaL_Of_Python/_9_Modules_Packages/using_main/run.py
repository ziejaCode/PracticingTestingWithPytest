

#print(f'Loading run.py:__name__ = {__name__}')

#import module1
from timing import timeit

code = '[x**2 for x in range(1_000)]'

result = timeit(code, 100)
print(result)