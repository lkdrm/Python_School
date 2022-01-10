#znamky:
znamky = [1,2,5,2,1,3,4,1]

psi = ["Alik","Rex","Teyla","Vorisek","Patrik"]

psi[3] = "Hugo"

print(psi[1:4])
print(psi[0:3])
print(psi[2:])
print(psi[:3])
print(psi[:])
print(psi[-1])
print(psi[1::2])

for i in psi:
    print(i)

for i in range(len(psi)):
    print(i)

for i in range(len(psi)):
    print(psi[i])

for i,pes in enumerate(psi):
    print("On index:", (i),"have", pes)


dog1,dog2,dog3,dog4,dog5 = psi

print(dog1)

car = ["Skoda", 2005,1.3,"Fabia"]

types,year,objem,model = car

cars = [["Skoda", 2005,1.3,"Fabia"],
        ["Volkswagen",2015,1.9,"Passt"],
        ["Mercedes",2010,2.2,"S"],
        ["Ferrari",2012,4.0,"formule"]]

print(cars[1][1])
print(cars[0][2])
print(cars[-1][-2])
print(cars[2][-4])

for car in cars:
    types,year,objem,model = car
    print(types,model,objem,year)

psi.remove("Hugo")
psi.append("Vincent")
psi.insert(4,"Hugo2")
psi.index("Rex")
psi.index("Vincent")