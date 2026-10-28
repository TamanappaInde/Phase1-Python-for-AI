class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee:", self.name)
        print("Salary: ", self.salary)

emp1 = employee("Tamanappa", 1000000)
emp2 = employee("Suraj", 2340000)

emp1.display_details()
emp2.display_details()

# class, object and method

