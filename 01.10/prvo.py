l = [1,2,3,4,5,6,7,8,9,10,11,12,13]   
new_prime = []
#Zjistuje jestli je prvocislo
def prime(a):
    for b in a:
        for i in range(2,b+1):
            if b%i == 0:
               return False
        return True

def prime_list(n_l):
    n_l = prime(a)

prime_list()
#print(new_prime)