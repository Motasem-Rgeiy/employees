class Employees:

    def __init__(self, id, first_name, last_name, age, salary , department):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__salary = salary
        self.department = department
    
    def employee_info(self):
        return f'ID:{self.id}, first name:{self.first_name}, Last_name:{self.last_name}, Salary:{self.__salary}'
    
    def set_salary(self, salary):
        if isinstance(salary , int):
            self.__salary = salary
            print('Salary has been modified.')
            return
        print('The salary must be an <Integer>')
    
    def get_salary(self):
        return self.__salary

        
employee1 = Employees('231054' , 'Motasem' , 'Rgyei' , 21 , 2500, 'IT')
print(employee1.get_salary())
    