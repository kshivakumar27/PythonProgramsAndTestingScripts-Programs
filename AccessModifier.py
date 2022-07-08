#Access modifiers

#public, private, protected

class Tiger():

    legs = 4
    __city = "bangalore"  #private variable
    _state = "karnatkae" #protected variable

    def playing(self):
        print("Tiger playing")

    def animal_sound(self):
        #super().animal_sound(self)
        print("overing animal sound BIG ROAR")

tiger = Tiger()

print(tiger._Tiger__city)

print(tiger._state)