class Elephant:
    def __init__(self,name,color,weight,called):
        self.name = name
        self.color = color
        self.weight = weight
        self.called = called

    def troubit(self):
        print("troubim")

    def water_on_people(self):
        if self.color == "pink":
            print("smile") 
        else:
            print("Polivam vodou lidi")

    def __str__(self):
        return f"The name of elephant {self.name} and he have a {self.color} color. And he have a weight {self.weight}"

    



first_elephant = Elephant("Mike","blue",1673,"Zoo")
first_elephant.troubit()
first_elephant.water_on_people()

print(first_elephant)

first_elephant.name = "Ajk"

print(first_elephant.name)

second_elephant = Elephant("Joe","pink",1200,"big")

print(second_elephant)

second_elephant.water_on_people()