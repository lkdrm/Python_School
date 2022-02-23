seznam = [ 6, 8, 9, 13]

# if this don`t exist = find, index, in


hledana_promena = 8

for cislo in seznam:
    if cislo == hledana_promena:
        print("Nalezeno")
        break
    print("neni")

# casova slozitost ?? == 2*n => n - linearni vyhledavani
# ukol udelat binarni vyhledavani