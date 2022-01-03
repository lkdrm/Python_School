"""
cislo = input("Enter the numb:")

for i in cislo:
    if i =="3" or i =="6":
        continue
    print(i,end=" ")
"""

import random

numb = random.randint(1,50)
count = 0

while True:
    tip = int(input("Which numb i created: "))
    count+=1
    if tip == 0:
        print("The numb is:",numb)
        print("End of programm")
        break
    elif tip == numb:
        print("Congrs")
        print("Your tries are",count)
        break
    elif tip < numb:
        print("The numb is bigger")
    else:
        print("The numb is lower")

