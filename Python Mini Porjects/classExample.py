class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def honk(self):
        print("Beep beep")

    def accelerate(self, rate):
        self.speed += rate

    def get_speed(self):
        return self.speed

my_car = Car("MarutiSuziki", "Baleno", 2018, 0)
my_car.honk()
my_car.accelerate(30)

print(my_car.get_speed())

