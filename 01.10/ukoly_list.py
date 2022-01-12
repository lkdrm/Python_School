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

def prime(b):
        for i in range(2,b):
            if b%i == 0:
                return False
        return True

def prime_list(ln):
    new_prime = []
    for number in ln:
        if prime(number):
            new_prime.append(number)
    return new_prime


print(prime_list(a))
