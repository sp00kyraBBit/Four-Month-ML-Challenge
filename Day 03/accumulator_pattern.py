raw_val = input("Enter a number: ")
try:
    val = int(raw_val)
    total = 0
    for i in range(val+1):
        total += i

    print("The summation is ",total)
except ValueError:
    print("Enter a valid number!!!")


