def decorator(func):
    def wrapper():
        print("Before Function Calling")
        func()
        print("After Function Calling")
    return wrapper
@decorator
def add(a,b):
    return a+b

add()