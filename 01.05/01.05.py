"""
#1 task:
def odd(a,b):
    for i in range(a,b):
        if i%2 == 1:
            print(i)

odd(0,30)
"""

"""
#2 task:

def symbs(leng,direc,symb):
    if direc == "horizont":
        print(symb*leng)
    elif direc == "vertical":
        a = (symb + "\n")*leng
        print(a)



symbs(10,"horizont","*")
symbs(8,"vertical","$")
"""

"""
#3 task:
def greater(a,b,c,d):
    l = [a,b,c,d]
    print("The greater is:",max(l))
    


greater(3,5,8,10)
greater(9,-50,25,0)
greater(-10,30,-2,10)

"""

"""
#4 task:
def sum_of_numb(a,b):
    sums = 0
    for i in range(a,b+1):
        sums += i
    print("The sum is:",sums)
    

sum_of_numb(2,5)
sum_of_numb(5,30)
"""

#5 task:

def prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

if prime(13):
    print("Je to prvocislo")
else:
    print("Neni prvocislo")