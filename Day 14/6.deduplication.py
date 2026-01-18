lst = [1,2,2,3]
seen = []
for num in lst:
    if num not in seen:
        seen.append(num)

print(seen)