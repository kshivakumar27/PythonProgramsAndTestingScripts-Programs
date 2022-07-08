legs = 4

def my_fun():
    global legs
    legs = 5
    print(f"legs inside method are {legs}")

my_fun()
print(f"legs outside method are {legs}")
