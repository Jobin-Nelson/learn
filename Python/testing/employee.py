import requests

class Employee:
    '''A sample Employee class'''
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'https://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname)

if __name__ == '__main__':
    emp_1 = Employee('Corey', 'Schafer', 5000)
    emp_2 = Employee('Test', 'Employee', 6000)

    Employee.set_raise_amt(1.05)

    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    import datetime
    my_date = datetime.date(2016, 7, 10)
    print(Employee.is_workday(my_date))

    dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
    dev_2 = Developer('Jane', 'Smith', 6000, 'Java')

    print(dev_1.email)
    print(dev_1.prog_lang)

    mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
    print(mgr_1.email)
    mgr_1.add_emp(dev_2)
    mgr_1.print_emp()
    print(isinstance(mgr_1, Employee))
    print(issubclass(Manager, Employee))
