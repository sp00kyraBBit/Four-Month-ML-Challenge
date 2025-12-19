In a **list**, the memory address assigned for any object is not determined through any hash function.  
Rather, the memory address for the first element is picked randomly, and then sequential memory addresses are assigned for the next elements.  
That’s why lists are **ordered**, and to look up an element we need to search through the list until we find the desired element.

Whereas the memory addresses assigned for a **set** or **dictionary** are determined through a **hash function**.  
We can think of this hash function as a magical mathematical function that selects the memory address for an element.  
If we need to know whether an element exists in a set or dictionary, we simply convert the element to its corresponding hash value (done internally) and check whether the object exists there.  
Because of this, lookup is **much faster**, but the objects are **unordered**.

**Reference:**  
[What makes sets faster than lists?](https://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists)