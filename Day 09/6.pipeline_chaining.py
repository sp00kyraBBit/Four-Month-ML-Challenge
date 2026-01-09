def square(num):
    for i in num:
        yield i**2

def filter(num):
    for i in num:
        if i%2==0:
            yield i

num = (x for x in range(10))
for i in filter(square(num)):
    print(i)
