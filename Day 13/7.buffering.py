with open("read.txt","a") as f:
    for i in range(1000000):
        f.write("Justice For Hadi!!!\n")

# python and OS uses buffering method while writing short and repetative data. It first store the data in RAM buffers
# when the ram buffer is full then it flush the whole chunk of the data in the disk at a time
# making efficient use of the disk rotation