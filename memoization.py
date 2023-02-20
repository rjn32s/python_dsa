from functools import wraps
from time import perf_counter
import sys

def memoize(func):

    cache = {}

    @wraps(func)
    def wrapper(*args , **kwargs):
        key  = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fibbo(n) -> int:
    if n<2:
        return n
    return fibbo(n-1)+fibbo(n-2)

if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    st = perf_counter()
    F = fibbo(3000)
    en = perf_counter()

    print(f"Time : {en-st} seconds")