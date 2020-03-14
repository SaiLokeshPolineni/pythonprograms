
#fc func -> func can be stored as variable
#can be passed as argument
#returns func from another func, can store n any data structure

def outer_func(tag):
    def inner_func(msg):
        return f'<{tag}>{msg}</{tag}>'
    return inner_func

f=outer_func("h1")
print(f)
print(f("Hello World"))
