class Elephant:
    def __init__(self,name,color,weight,called):
        self.name = name
        self.color = color
        self._weight = weight # that means, that its constant
        self.called = called
        if self._weight < 15:
            self.fly = True
        else:
            self.fly = False

    def troubit(self):
        print("troubim")

    def water_on_people(self):
        if self.color == "pink":
            print("smile") 
        else:
            print("Polivam vodou lidi")
    
    def set_weight(self,new_weight):
        self._weight = new_weight
        if self._weight < 15:
            self.fly = True
        else:
            self.fly = False

    def __str__(self):
        return f"The name of elephant {self.name} and he have a {self.color} color. And he have a weight {self._weight}"

    
jumbo = Elephant("Jumbo","blue",30,"Zoo")
jumbo.troubit()
jumbo.water_on_people()

print(jumbo)

#first_elephant.name = "Ajk"

print(jumbo.name)

dumbo = Elephant("Dumbo","pink",1200,"big")

print(dumbo)

dumbo.water_on_people()

jumbo._weight = 11

dumbo.set_weight(10)

print(dumbo.fly)
print(jumbo.fly)