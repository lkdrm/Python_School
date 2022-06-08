#cycly for

slovnik = {"klic":23,"klic2":65, "klic":213}

for neco in slovnik:
    print(neco)

#while
index = 0
slovnik = [2,5,7]

while index < len(slovnik):
    print(slovnik(index))
    index +=1

##
seznam = [2,34,76,1]
iterator = iter(seznam)

###
#gen

def my_generator():
    yield 5
    print("Hello")
    yield 6

gen = my_generator()
print(gen)
####

seznam = [1,2,3,4,5]
novy_seznam = [i*i for i in seznam] # list compr
novy_seznam_2 = (i*i for i in seznam) # generator expession
#####
