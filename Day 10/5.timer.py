import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        print(time.time() - start)
    return wrapper

@timer
def hello():
    for i in range(1000000):
        if i==-1:
            break
    print("Hello Shahriar")

hello()