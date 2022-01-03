"""

def hello(name):
    print(" ")
    print("Hello",name)
    print("Put your shoes behinde")
    print("Go toward to the room")

hello("Kile")
hello("Marta")
hello("Djek")

"""
"""
def count(a,b):
    print("Count numbs:", a,"and", b)
    sum = a + b 
    return "The sum is " + str(sum)


print(count(5,8))
"""
#2 task:
"""
def hello(guess):
    return "Hello " + guess

print(hello("Kile"))
print(hello("Mike"))
print(hello("Kartman"))

"""
#3 task:
"""
def count(a,b):
    sum = a + b
    return "The sum is :" + str(sum)

first_sum = count(5,6)
second_sum = count(3,20)
third_sum = count(5,9)
print(first_sum)
print(second_sum)
print(third_sum)
"""
#4 task:
#Vepocet:
"""
def count(a,b):
    sum = a*b
    return sum

first_numb = count(8,7)
print("The sum is:",first_numb)

second_numb = count(5,6)
print("The sum is:",second_numb)

print("The sum of first and second numb is:",first_numb*second_numb) 
"""
#5 task:

# Napište funkci, která bere tři parametry. První a druhý parametr jsou čísla, se kterými se bude
# počítat. Třetí parametr určí operaci ( 1 - sčítání, 2 - odčítání, 3 - násobení). Nic se netiskne,
# výsledek se vrací pomocí return.
"""
def count (a,b,c):
    if c == 1:
        sum = a + b
        return sum
    elif c == 2:
        sum = a - b
        return sum
    elif c == 3:
        sum = a*b
        return sum

print("Scitani:",count(2,3,1))
print("Odcitani",count(5,2,2))
print("Nasobeni",count(5,5,3))

"""
#6 task:
#Napište funkci kalkulacka (můžete použít kód z dřívějška) - funkce se vždy zeptá na dvě čísla a na 
#třetí číslo jako operaci. Operace je 0 - skončit, 1 - sčítání, 2 - odčítání atd. Po provedení 
#operace se vytiskne výsledek a kalkulačka se zeptá na další zadání. Skončí jen po zadání nuly jako 
#operace. Funkci zavolejte.


def count():
    while True:
        a = int(input("Enter the first numb: "))
        b = int(input("Enter the second numb: "))
        c = int(input("what to do : "))
        if c == "+":
            sum = a + b
        elif c == "-":
            sum = a - b
        elif c == "3":
            sum = a*b
        print(sum)


count()

