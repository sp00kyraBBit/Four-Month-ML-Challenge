with open("read.txt","w") as f:
    f.write("Hello Shahriar!!!")    #....removes the previous contents of the file if exists

with open("read.txt","a") as f:
    f.write("\nHow was your day?")  #....updates the existing file

# with open("read.txt","x") as f:
#     f.write("Can't Open")    # can't open a file if it already exists


# Adding the log line
with open("read.txt","a") as f:
    f.write("Day 13: I am learning I/O operation in python")