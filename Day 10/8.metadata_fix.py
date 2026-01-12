def my_decorator(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add.__name__)


## fix
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add.__name__)

