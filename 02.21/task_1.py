#2 task:
soubor_na_cteni = open("practice.txt","r")

obsah_souboru = soubor_na_cteni.readlines()

soubor_na_cteni.close()

#print(obsah_souboru)

soubor_na_zapis = open("sem_to_zapis.txt","w")

soubor_na_zapis.writelines(obsah_souboru)

soubor_na_zapis.close()
#################

soubor_na_cteni = open("practice.txt","r")
soubor_na_zapis = open("sem_to_zapis.txt","w")


for i in soubor_na_cteni:
    soubor_na_zapis.write(i)


soubor_na_cteni.close()
soubor_na_zapis.close()

with open("sem_to_zapis") as soubor_pro_terminal:
    print("Vypisuji vysledek")
    #for i in soubor_pro_terminal:
    #    print(i, end="")
    print(soubor_pro_terminal.read())
################

#with open("practice.txt","r") as soubor_na_cteni, open("sem_to_zapis.txt","w") as soubor_na_zapis:
#    for i in soubor_na_cteni:
#        soubor_na_zapis.write(i)

