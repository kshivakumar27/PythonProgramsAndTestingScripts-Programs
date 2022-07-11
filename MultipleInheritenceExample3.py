class Lion:
    def lion_sound(self):
        print("lion sound")

    def playing(self):
        print("lion playing")

class Tiger():

    legs = 4
    city = "bangalore"
    state = ""

    def playing(self):
        print("Tiger playing")

    def animal_sound(self):
        #super().animal_sound(self)
        print("overing animal sound BIG ROAR")



    def tiger_roar(self, country):
        print("tiger roars")
        print(f"tiger is from {self.city} and state is {self.state} and countyr is {country}")


class Cub(Tiger, Lion):
    def cub_sound(self):
        print("cub makes sound")

cub = Cub()
