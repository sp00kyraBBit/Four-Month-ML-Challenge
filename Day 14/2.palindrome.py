def palindrome(str):
    temp = "".join(x.lower() for x in str if x.isalnum())
    return temp == temp[::-1]

print(palindrome("Race Car"))