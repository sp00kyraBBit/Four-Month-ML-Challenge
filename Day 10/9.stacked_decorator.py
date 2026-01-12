def bold(func):
    def wrap():
        return "<b>" + func() + "</b>"
    return wrap

def italic(func):
    def wrap():
        return "<i>" + func() + "</i>"
    return wrap

@bold
@italic
def text():
    return "Hello Shahriar"

print(text())
