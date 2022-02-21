with open("practice.txt","r") as soubor_na_cteni:
    obsah_souboru = soubor_na_cteni.readlines()


obsah_souboru.reverse()
print(obsah_souboru)


with open("sem_to_zapis_2.txt","w") as soubor_na_zapis:
    soubor_na_zapis.writelines(obsah_souboru)
