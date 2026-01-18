lst = range(1,101)
for num in lst:
    if num%15==0:
        print(num,": FizzBuzz")
    elif num%3==0:
        print(num,": Fizz")
    elif num%5==0:
        print(num,": Buzz")