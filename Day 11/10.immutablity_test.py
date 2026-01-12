tup = tuple(range(5))

try:
    tup[3] = 0
except TypeError:
    print("Tuples are immutable")