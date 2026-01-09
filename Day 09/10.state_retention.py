def running_avg():
    print("Started")
    count = 0
    total = 0
    while True:
        value = yield
        total += value
        count += 1
        avg = total/count
        print(f"The average is {avg}")

a = running_avg()
next(a)
a.send(4)
a.send(10)
a.send(16)