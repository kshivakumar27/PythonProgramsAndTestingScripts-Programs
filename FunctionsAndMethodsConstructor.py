class Tiger:



#in python there is not constructor overloading nor method overloading



    legs = 4
    city = "bangalore"
    state = ""



def __init__(self,state):
    self.state = state



def tiger_roar(self):
    print("tiger roars")
    print(f"tiger is from {self.city} and state is {self.state}")



tiger = Tiger()
#tiger.tiger_roar()