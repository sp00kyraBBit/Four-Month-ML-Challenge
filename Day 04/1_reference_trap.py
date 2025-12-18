a = [1,2,3]
b = a
b[0] = 99
print("Before making a shallow copy: ", a)

# fix: making a shallow copy
a = [1,2,3]
b = a.copy()
b[0] = 99
print("After making a shallow copy ", a)

# Another Fix
a = [1,2,3]
b = a[:]
b[0] = 99
print("After making a shallow copy ", a)
