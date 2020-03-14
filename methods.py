class Employee:
    employee_id = 775831
    def __init__(self,name,salary):
        self.name = name
        self.emp_id = Employee.employee_id
        self.salary = salary
        Employee.employee_id += 1

    def display(self):
        ''' Regular Method to Display emp details'''
        return f'Id: {self.emp_id}, Name: {self.name}, Salary: {self.salary}'

    @classmethod
    def set_attr(cls, details):
        '''Class method to intalize class'''
        name, salary = details.split()
        return cls(name, salary)

    @staticmethod
    def company_details():
        '''static method doesn't rerquire any reference to class or instance, so no parameters and no usage of self'''
        return f'Infosys, Lead to Tomorrow'
s1="Lokesh 32000"
s2="Praveen 58000"
l=[s1,s2]
for i in l:
    c=Employee.set_attr(i) #Calling classmetod to initialize instead of init
    print(c.company_details())
    print(c.display())