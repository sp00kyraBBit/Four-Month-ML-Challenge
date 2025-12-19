"""
In list the memory address assigned for any object is not determined through any hash function.
Rather the memory address for the first element is picked randomly and then sequentially memory addressed are assigned for the
next elements that's why the lists are ordered and to look up an element we need to search through the list until we find the
desired element.

Whereas the memory address assigneed for the set/dict are determined through a hash function. We can say this hash function as
a magical mathematical function to select the memory address for an element. Now if we need to know that some element is in the 
set/dictionary or not we just need to convert the element to it's corresponding hash value(done internally) and check whether 
the object exists there. So the lookup is very faster but objects are unordered.


Reference: https://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists
"""

lst = list(range(-500000,500000))
set_lst = set(lst)
for i in lst:
    if i == -1:
        print("Element found")
        break

if -1 in set_lst:
    print("Element found")
else:
    print("Element not found")