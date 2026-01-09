def large_file_reader(path):
    with open(path,'r') as file:
        for line in file:
            yield line

file = large_file_reader("memory.txt")
# for line in file:
#     print(next(file))
print(next(file))
print(next(file))
print(next(file))

