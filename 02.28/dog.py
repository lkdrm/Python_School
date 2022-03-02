# trida se pise z velkeho pismena
# je to trida 
class Dog:
    #dunder metody
    def __init__(self,name,called, weight):
        self.name = name #field
        self.called = called #field
        self.weight = weight

    def wuf(self):
        print("Haf haf haf")
    
    def kousej(self):
        print("Chrast chrast chrast")

    def __str__(self):
        return f"My name is {self.name} and i`m a {self.called} "
"""
alik_1 = Dog()

print(alik_1)

alik_1.wuf()
print(alik_1.name)

alik_1.name = "Max"

print(alik_1.name)

alik_1.called = "find dog"

alik_7 = Dog()

alik_7.called = "save dog"

print(alik_1)

print(alik_7)
"""

alik_1 = Dog("Ajk","Saved dog", 15)

print(alik_1.name)

alik_1.kousej()

alik_2 = Dog("Rex","little dog",5)

print(alik_2.called)


print(alik_1)