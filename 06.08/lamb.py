def dvakrat(cislo):
    return cislo *2

print(dvakrat(2))

dvojnasobek = lambda x : x *2

print(dvojnasobek(2))
######################

def identita(cislo):
    return cislo

id2 = lambda x : x
#####################

def pejsek():
    return "haf haf haf"

pes = lambda : "haf haf haf"
(lambda x,y,z : x + 5 + 2 *y - z)(3,4,10)

def scitej(cislo1, cislo2):
    return cislo1 + cislo2

scitani = lambda x,y : x + y


def uprav(text):
    return text.lower().capitilize()

uprav2 = lambda text : text.lower().capitilize()