seznam = [2,5,6,7,9]

def na_druhou(cislo):
    return cislo * cislo

novy_seznam = list(map(na_druhou,seznam))

novy_seznam_2 = list(map(lambda x: x*x, seznam))
print("Novy seznam :", novy_seznam)
print("Novy seznam 2 :", novy_seznam_2)

novy_seznam_3 = list(filter(lambda x : x >5, seznam))
#map , filter, reduce.

seznam_2 = [(2,6), (3,13), (5,9), (7,3), (4,0)]

print(sorted(seznam_2, key = lambda x : x[1]))

slova = ["jablko","ananas","Eva","Boris","rajce"]

print(sorted(slova,key=lambda s : s.lower()))
print(sorted(slova, key=len))