from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 2:
        return n
    print("N-1", fibonacci(n-1))
    print("N-2", fibonacci(n-2))
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))