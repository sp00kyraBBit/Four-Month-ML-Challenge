lst = [3,2,4]
target = 6
s = dict()
for num in lst:
    if (target - num) in s:
        print(num, target-num)
    s[num] = 1