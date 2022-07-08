#print("hello");



class Tiger:
    legs = 4
    city = "bangalore"
    
    def tiger_roar(self):
      print("tiger roars")

tiger = Tiger()
print(f"tiger from city {tiger.city}")
print(tiger.legs)

tiger.tiger_roar()