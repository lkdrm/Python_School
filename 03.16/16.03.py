import numpy as np

my_list = [2, True, "Tree", 22, 9.0,]

pole1 = np.array([1,3,5,6,8,9])

type(pole1)

pole1.size

pole1.shape
pole1.sum()

pole1.append(5)
pole1[2:4]

pole1 + 10

np.zeros(6)
np.zeros((6,7))

np.ones((5,4))

np.full(3,7)
np.empty(3)

np.arange(0,10)

pole2 = np.arange(14)
pole2.reshape((3,5))

np.linspace(1,5,15)

print(pole1.max())

print(pole2.sum())

nove_pole = pole2 + 15