class Mammal:
    mamal_legs = 4
    def mammal_sound(self):
        print("mamal makes sound")

class Animal(Mammal):
    animallegs = 4
    def animal_sound(self):
        print("Animal makes sound")


class Tiger(Animal):

    legs = 4
    city = "bangalore"
    state = ""

    def animal_sound(self):
        #super().animal_sound(self)
        print("overing animal sound BIG ROAR")

    def __init__(self,state):
        self.state = state

    def tiger_roar(self, country):
        print("tiger roars")
        print(f"tiger is from {self.city} and state is {self.state} and countyr is {country}")

tiger = Tiger("karnataka")
tiger.animal_sound()
tiger.mammal_sound()
