def genN():
    yield 1
    yield 2
    yield 3

def genL():
    yield "a"
    yield "b"

def genNL():
    yield from genN()
    yield from genL()

for i in genNL():
    print(i)