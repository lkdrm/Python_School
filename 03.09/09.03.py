#Dedicnost - inheritans

class Humans: #Superclass
    """ This is a class which created a humans """ # always must to comment what this class do. docstring
    def __init__(self,name:str,year:int):
        self.name = name
        self.year = year
    
    def __str__(self):
        return f"My name is {self.name} & i`m {self.year} years old"

    def hello(self):
        return "Hello , how are you?"

    def sleep(self):
        return "chrr"


class Programmer(Humans): # trida Prohramator dedi Humans ## Subclass
    def __init__(self,name,year,lang:str,):
        name = "Superman" + name
        super().__init__(name,year+2)
        self.lang = lang

    def drink_coffee(self):
        return "I like to drink coffee"

    def say_hi(self):
        return "Hi"

    def sleep_prog(self):
        return "I sleep & dream about OOP"

    def __str__(self):
        return f"I`m a programator {self.name} & I like code in {self.lang}"



class Manazer(Humans):
    def __init__(self, name: str, year: int):
        super().__init__(name,year)

    def sleep_prog(self):
        return "Sleep & dream how i fire a worker"

erik = Programmer("Erik",35,"Javascript")
joe = Programmer("Joe",20,"Python")
pepa = Humans("Joseph",18)
hugo = Manazer("Hugo",40)


my_list = [erik,joe,pepa,hugo,]

print(erik.sleep())
print(erik.hello())
print(erik.drink_coffee())
print(erik.say_hi())
print(erik)

print(joe)
print(hugo)

for person in my_list:
    print(person)
