lst = list(range(-5,5))

print(any(x<0 for x in lst))
print(all(x>0 for x in lst))