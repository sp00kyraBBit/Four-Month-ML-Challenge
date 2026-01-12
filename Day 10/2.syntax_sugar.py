def decorator(func):
    def inner():
        print("Before Function Calling")
        func()
        print("After Function Calling")
    return inner
@decorator
def name():
    print("Hello Shahriar")

name()