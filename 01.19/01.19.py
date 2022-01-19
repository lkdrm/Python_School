# dictionary
# docs.python.org
# get(key, here i write if key not in dict)

# items - do that show you key and values

for key,value in dict.items():
   print (key,value)



dog = {"name1":"dog",
        "name2":"dog2",}

for key,value in dog.items():
    print(key,value)


#########

# tuple:


seznam = ["Alik","Rex","Bert"]

tupple = ("Micka","Liza","Chubaka")

print(seznam[0])
print(tupple[2])

print(seznam[1:])
print(tupple[1:])

seznam[0] = "Zly vlcak"

tupple[0] = "Hodna kocicka"
###################################

slovnik = {
    2:"dvojka",
    "s":"pismo s",
    True:"boolean",
    (1,2,3):"seznam tri cisel",
    (1,2,3[4,8],7): "tuple s vlozenim" # will write error
}

#################

#Set :

my_set = {1,2,3,1,2,2,4,5,6,2,3,4,5,6,2}
print(my_set)

seznam = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,]
print(set(seznam))

my_set2 = set(seznam)
seznam2 = list(my_set2)
print(seznam2)

my_set3 = {2,3,8,9,12}

print(my_set.intersection(my_set3))
print(my_set.union(my_set3))

my_set.add(20)
my_set.remove(5)

print(my_set | my_set3)