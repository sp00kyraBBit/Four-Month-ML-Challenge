import sys

list_comp = [x for x in range(1000000)]
print(f"list comprehension consumes {sys.getsizeof(list_comp)} bytes.")

gen_expres = (x for x in range(1000000))
print(f"generator expression consumes {sys.getsizeof(gen_expres)} bytes.")