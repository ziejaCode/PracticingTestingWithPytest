# timing

print('Loading timing...')

from time import perf_counter
from collections import namedtuple

Times = namedtuple('Timing', 'repeat elapsed average')

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed/repeats
    return Times(repeats, elapsed, average)