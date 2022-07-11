class Tiger():

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


class Cub(Lion, Tiger):
    def cub_sound(self):
        print("cub makes sound")

cub = Cub()
cub.lion_sound()
cub.tiger_roar()