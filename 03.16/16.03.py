import numpy as np

my_list = [2, True, "Tree", 22, 9.0,]

pole1 = np.array([1,3,5,6,8,9])

type(pole1)

pole1.size

pole1.shape
pole1.sum()

pole1.append(5)
pole1[2:4]

pole1 = pole1 + 10 # to array add to everyone + 10

li_of_zeros = np.zeros(6) # created a array of 6 zeros
li_of_zeros__2 = np.zeros((6,7))  # created a chart

li_of_ones = np.ones((5,4)) # same as a zeros but with numbers 1

li_of_numbers = np.full(3,7) # created a list with a [ 7 7 7 ]
np.empty(3)

li_of_range = np.arange(0,10) # created a list of range from 0 to 9

pole2 = np.arange(14)
pole2.reshape((3,5))

np.linspace(1,5,15)

print(pole1.max())

print(pole2.sum())

nove_pole = pole2 + 15
