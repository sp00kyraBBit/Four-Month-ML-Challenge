def decorator(func):
    def wrapper(*args):
        func(*args)
    return wrapper
@decorator
def add(a,b):
    return a+b

print(add(4,5))