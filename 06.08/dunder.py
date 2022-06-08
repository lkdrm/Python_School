class Hroch:
    def __init__(self, name, length_oc):
        self.name = name
        self.length_oc = length_oc

    def __len__(self):
        return self.length_oc

    def __add__(self,other):
        return self.length_oc + other.length_oc

    def __mul__(self,other):
        self.length_oc /= 2
        other.length_oc /=2
        return self.length_oc + other.length_oc

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        self.index +=1
        if self.index >= len(self.name):
            raise StopIteration
        return self.name[self.index]
        

    def __str__(self):
        return f"I`m a {self.name} & have {self.length_oc} ears"



adam = Hroch("Adam",20)
borek = Hroch("Borek",26)
cyril = Hroch("Cyril",5)
print(len(adam))
print("Sum :",borek+cyril)
print(adam*borek)

for x in adam:
    print(x)