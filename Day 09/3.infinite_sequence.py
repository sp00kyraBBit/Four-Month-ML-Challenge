def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
a= fib()
for i in range(20):
    print(next(a))
