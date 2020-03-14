
class Sentence():
    def __init__(self, s):
        self.sentence = s
        self.index = 0
        self.words=self.sentence.split()

    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]
c=Sentence("Hello I am here")
print(next(c))
print(next(c))
print(next(c))

