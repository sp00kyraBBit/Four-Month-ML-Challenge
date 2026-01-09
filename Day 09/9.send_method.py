def gen():
    print("Started")
    value = yield
    print(value)

a = gen()
next(a)
a.send(4)


