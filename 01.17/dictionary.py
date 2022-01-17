anglictina = {
    "apple": "jablko",
    "car":"auto",
    "book":"kniha",
    "table":"stul",
    "flower":"kvetina"
}

print(anglictina["apple"])

pavluv_slovnik = {
    "jmeno":"Pavel",
    "vek":35,
    "oblibena barva":"zluta",
    "vyska":180,
    "pije_rad_pivo":True,
    5:"nevim co sem napsat"
}


for key in anglictina.keys():
    print(key)

for value in anglictina.values():
    print(value)


for itemss in anglictina.items(): # is tuple
    print(itemss)

for klic,hodnota in anglictina.items():
    print("klic je:", klic,"\n","a hodnota je:", hodnota ,)

keys = anglictina.keys()
val = anglictina.values()
polozky = anglictina.items()

print(keys)
print(val)
print(polozky)


seznam = ["Alik","Rex","Bert"]

for index,item in enumerate(seznam):
    print(index,"----",item)

for dvojce in enumerate(seznam):
    print(dvojce)