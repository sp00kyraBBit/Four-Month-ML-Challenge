lst = [1,2,3,4,5,6,7,8]
target = 3
left = 0
right = len(lst)
idx = -1
mid = round((left + right)/2)
while True:
    if lst[mid] > target:
        right = mid
    elif lst[mid] < target:
        left = mid
    elif lst[mid] == target:
        idx = mid
        break
    elif left == right:
        break
    mid = round((left + right)/2)
print(idx)