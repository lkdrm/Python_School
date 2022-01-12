# The user types in a list of integers. Calculate the sum and 
# average of these elements. 
# Print the result:
"""
a = [1,2,3,4,5]

def sum_of_numb(my_list):
    return(sum(my_list))

def average(list_of_numbers):
    leng_of_numb = len(list_of_numbers)
    return sum_of_numb(list_of_numbers) / leng_of_numb 

print(sum_of_numb(a))
print(average(a))

"""
def factorial(number):
    if number <=1:
        return 1
    vysledek = number * factorial(number - 1)
    return vysledek

print(factorial(5))


################
"Practice modul 3 part 3 vše"
# Task 1:
# Calculate the following in a list filled with random numbers:
# ■ Sum of negative numbers;
# ■ Sum of even numbers;
# ■ Sum of odd numbers;
# ■ Product of elements with indices divisible by 3;
# ■ Product of elements between the smallest and the largest 
# element;
# ■ The sum of the elements between the first and the last 
# positive elements.

# Task 2:
# There is a list of integers filled with random numbers. Do 
# the following based on this data:
# ■ Create a list of integers containing only even numbers;
# ■ Create a list of integers containing only odd numbers;
# ■ Create a list of integers containing only negative numbers;
# ■ Create a list of integers containing only positive numbers

import random

random_number = random.randrange(1,30)

def sum_of_numbers(my_number):
