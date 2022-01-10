#1 Fisrt task:
a = [1,2,3,4,5,6,7,8,9]
b = [2,4,6,8,9,]

def calk(l):
    print(sum(l))

calk(a)
calk(b)

#2 second task:
"""
a = [-2,4,5,-10,3,2]
b = [2,5,8,123,-10]
def min_l(l):
    print(min(l))

min_l(a)
min_l(b)

"""
#3 third task:
a = [1,2,3,4,5,6,7,8,9,10]   

#Zjistuje jestli je prvocislo
def prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

prime(a)

def prime_list():
   #посилаю до прайм и сюда повертае
prime(a)