#1 First task:
word = "python"

def cut(word):
    new_list = []
    for i in word :
        new_list.append(i)
    return "".join(sorted(new_list))

print(cut(word))
# or :
sorted(word)
# or :
list(word)

#2 Second task:
my_set = [1,1,2,4,5,8,9,5,0,6]

change = set(my_set)
print(len(change))

#3 Third task:

my_list = [1,2,3,4,5,6]
my_list_2 = [2,4,6,8,10]

def number_plus_one(my_list):
    new_list = []
    for i in my_list:
        i+=1
        new_list.append(i)
    return new_list

print(number_plus_one(my_list))
print(number_plus_one(my_list_2))
# better :
    # list compression :

my_list = [2, 4, 6, 8, 10]
new_list = [number + 1 for number in my_list]
print(new_list)

#########################################

try:
    delenec = int(input("write first number:"))
    delitel = int(input("Write a second number:"))
    
    vysledek = delenec / delitel

    print(f"Vysledek je {vysledek}")
except ZeroDivisionError : 
    print("Tou can`t devide by zero")
except ValueError:
    print("Number can`t devide by value")
except KeyboardInterrupt:
    print("Please write a number")
except:
    print("We have a error") 

print("End of programm")

###########################################
my_list = [1,5,6,8,1,2,3,9,4,5,6]

try:
    print(my_list[50])
except IndexError as word:
    print(f"We have a problem: {word}")

###########################################
from time import sleep

seconds = 0
"""
while True:
    try:
        seconds +=1
        print(f"Now was {seconds} second.")
        sleep(1)
    except KeyboardInterrupt:
        print("Ha ha ha ha - this program can`t stop")
"""
###############################################
my_string = "Hello"
"""
while True:
    try:
        my_string = 2 * my_string
    except MemoryError:
        print("I have`t enough memory ")
        break
"""

##############################################

number = 5 * 6
number +=10
number *= 2

try:
    assert number == 60
except AssertionError:
    print(f"Number isn`t same as : {number}")

print("All okay")

##############################################
my_list = [1,2,3,4,5]

new_list = [number + 5 for number in my_list ]
print("New list is :", new_list)

new_list_2 = [number **2 for number in my_list]
print(f"New list is : {new_list_2}")

new_list_3 = [
    number ** 2
    for number in my_list
    if number %2 == 0 
]      
print(new_list_3)

############################################################
my_list_4 = ["ahoj", "ovoce", "zelenina", "brambory"]

new_word_list = []

for word in my_list_4:
    for letter in word:
        new_word_list.append(letter)

print(new_word_list)

new_word_list_compresion = [
    letter
    for word in my_list_4
    for letter in word
]
print(new_word_list_compresion)

my_list_4 = ["ahoj", "ovoce", "zelenina", "brambory"]

new_word_set_compression = {
    letter
    for word in my_list_4
    for letter in word 
}

print(new_word_set_compression)

my_list = [1,2,3,4,5]

keys_list_compresion = {
    number : number ** 2
    for number in my_list
}

print(keys_list_compresion)

