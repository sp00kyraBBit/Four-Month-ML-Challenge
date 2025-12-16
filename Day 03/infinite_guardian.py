# takes user input as a password indefinitely
while True:
    password = input("Enter Your Password: ")
    if password == "stop": # if gets "stop" it breaks out of the loop
        break
