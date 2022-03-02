class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color.capitalize()} {self.model}"

punta = Car("Skoda","blue")

bourak = Car("Mercedes", "black")

print(punta)
print(bourak)


class Human:
    def __init__(self, name: str, weight: int, car: Car):
        self.name = name
        self.weight = weight
        self.car = car

    def __str__(self):
        return f"My name is {self.name} and I have a {self.car}."


Anny = Human("Anny",45,bourak)

Pepa = Human("Pepa",90,punta)

Honza = Human("Honza", 80, Car("trabant","green"))

print(Anny)

print(Pepa)

print(Honza)

print(Pepa.name)
print(Anny.car.color)
"has - a"