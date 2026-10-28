class Retangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rec1 = Retangle(200, 100)

print(rec1.calculate_area())


