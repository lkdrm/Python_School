# udelej druhe mocniny cisel v seznamu a pak jejich soucet 
seznam = [1,2,3,4,5,6]


druhy_mocniny = [
    number ** 2 
    for number in seznam
]

suma = sum(druhy_mocniny)
print(suma)

#better version:
seznam = [1,2,3,4,5,6]
# generator:
druhy_mocniny = sum(
    number ** 2 
    for number in seznam
)

print(druhy_mocniny)