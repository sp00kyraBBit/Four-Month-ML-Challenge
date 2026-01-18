def flatten(lst):
    flat_lst = []
    for x in lst:
        if isinstance(x,list):
            flat_lst+= flatten(x)
        else:
            flat_lst.append(x)
    return flat_lst

print(flatten([[1,2],[3,4]]))