def wrapper(func):
    def inner():
        print("Before Function Calling")
        func()
        print("After Function Calling")
    return inner
    
def name():
    print("Hello Shahriar")

new_func = wrapper(name)
new_func()

