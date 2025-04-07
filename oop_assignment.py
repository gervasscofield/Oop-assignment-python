# --------------------------------------
# 🏗️ Assignment 1: Design Your Own Class
# --------------------------------------

class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def show_power(self):
        print(f"{self.name} uses {self.power} with strength level {self.strength}!")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, fly_speed):
        super().__init__(name, power, strength)
        self.fly_speed = fly_speed

    def fly(self):
        print(f"{self.name} is flying at {self.fly_speed} km/h!")


# Create instances and test
print("\n--- Superhero Demo ---")
hero1 = Superhero("StormBreaker", "Thunder Smash", 95)
hero2 = FlyingSuperhero("SkyFire", "Blazing Light", 85, 120)

hero1.show_power()
hero2.show_power()
hero2.fly()


# --------------------------------------
# 🎭 Activity 2: Polymorphism Challenge
# --------------------------------------

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


# Create instances and test polymorphism
print("\n--- Vehicle Polymorphism Demo ---")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
