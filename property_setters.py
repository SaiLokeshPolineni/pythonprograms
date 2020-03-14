class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first+"."+last+"@company.com"         #Use property decorator for same func

    @property
    def email(self):
        return self.first+"."+self.last+"@company.com"

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.deleter
    def fullname(self):
        print("Here we are deleting!")
        self.first = None
        self.last = None

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


c=Employee("SaiLokesh", "Polineni")
print(c.fullname)
print(c.email)  #No need to menton() property dec handles that
c.fullname="Avinash Polineni"
print(c.fullname)
print(c.email)
del c.fullname
print(c.fullname)
print(c.email)
