
def sentence(s):
    words=s.split()
    for i in words:
        yield i

a="Hello i am here"
l=sentence(a)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))