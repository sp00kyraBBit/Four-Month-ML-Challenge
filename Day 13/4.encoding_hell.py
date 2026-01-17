with open("read.txt","r") as f:
    data = f.read()
    print(data)  


# output:
# Hello Shahriar!!!
# How was your day?Day 13: I am learning I/O operation in pythonðŸ˜‘ðŸ˜‘

# Fix unicodedecoderror
with open("read.txt","r",encoding="utf-8") as f:
    data = f.read()
    print(data)

# output:
# Hello Shahriar!!!
# How was your day?Day 13: I am learning I/O operation in python😑😑