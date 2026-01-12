lst = ["100px","20px","3px"]

sorted_lst = sorted(lst, key=lambda x: int(x[:-2]))

print(sorted_lst)