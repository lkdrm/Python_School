a = [1,2,3,4,5,6,7,8,9,10,11,12,13]   

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
