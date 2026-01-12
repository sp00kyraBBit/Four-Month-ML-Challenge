def memo(func):
    cache = {}
    def wrap(n):
        if n in cache:
            return cache[n]
        cache[n] = func(n)
        return cache[n]
    return wrap

@memo
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))