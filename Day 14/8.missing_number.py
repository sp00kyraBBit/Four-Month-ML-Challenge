lst = list(range(1,101))
lst.remove(55)
summation = sum(lst)
n = len(lst)+1
missing_number = ((n*(n+1))/2) - summation
print(missing_number)