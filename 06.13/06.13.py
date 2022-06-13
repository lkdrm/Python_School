# position arguments = *args
# keyword arguments = **kwargs

def prumer(*args):
    return sum(args) / len(args)

print(prumer(8,5,3))

def vytisk(*args):
    print

#####################
# First class citizen

def pozdrav():
    print("Ahoj jak se mas.")

def pozdrav_slusne():
    print("Dobry den jak se mate?")

pozdravy = [pozdrav,pozdrav_slusne]

print(pozdravy[1]())
#####################

def pozdrav(jmeno):
    print(f"Ahoj {jmeno}, jak se mas? ")

def pozdrav_slusne(prijmeni):
    print(f"Dobry den pane/pani {prijmeni} , jak se mate?")

def funkce_co_zdravi(f,jmeno):
    return f(jmeno)


print(pozdrav, "Honzo")

def pocasi(kod):
    def sluneco():
        print("Dnes je slunicko.")
    
    def destivo():
        print("Dnes prsi.")
    
    print("Skoncila funkce pocasi.")
    
    if kod == 1:
        return sluneco
    else:
        return destivo


###################
import functools
# Decoratory
def muj_dekorator(fce):
    @functools.wraps(fce)
    def wrapper(*args,**kwargs):
        print("Tohle se stane pred funkci.")
        vysledek=fce(*args,**kwargs)
        print("Tohle se stane po fukci.")
        return vysledek
    return wrapper

@muj_dekorator
def pozdrav(jmeno,prijmeni,vek):
    """Tohle je funkce, ktera umi pozdravit."""
    print(f"Ahoj {jmeno} {prijmeni} jak se mas.Dnes je ti {vek} let")
    return 43

#pozdrav = muj_dekorator(pozdrav)

print(pozdrav("Honza","Novotny", vek=29))
###########
import functools

def udelej_dvakrat(fce):
    @functools.wraps(fce)
    def dvakrat_wrapper(*args, **kwargs):
        fce(*args, **kwargs)
        return fce(*args, **kwargs)
    return dvakrat_wrapper

@udelej_dvakrat
def stekej():
    print("haf haf haf")
    print("konec stekani")
    print()

stekej()