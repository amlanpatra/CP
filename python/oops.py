class Employee:
    raise_amount = 1.04
    total_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+last + "@company.com"
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def raise_amt(cls, price):
        cls.raise_amount = price


emp1 = Employee("Amlan", "Patra", 1900)
emp2 = Employee("Rama", "Patra", 30000)
print(emp1.raise_amount)
Employee.raise_amt(2)
print(emp1.raise_amount)
