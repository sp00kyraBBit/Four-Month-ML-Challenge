from functools import reduce
lst = list(range(1,5))

prod = reduce(lambda x,y:x*y,lst)
print(prod)

