import numpy as np

x1 = np.random.randint(1, 10, size=6)  # creates a list of random numbers in 6 columns
x2 = np.random.randint(1, 10, size=(3, 4))  # creates a list with 3 rows adn 4 columns
x3 = np.random.randint(1, 10, size=(3, 4, 5))  # creates a list with 3 tables of 4 rows and 5 columns

print(x1)
print()
print(x2)
print()
print(x3)
print()
print(f"x3 ndim : {x3.ndim}") # finds the dimensions of the numpy array
print(f"x3 shape : {x3.shape}") # finds the shape of the numpy array
print(f"x3 size : {x3.size}") # find the size of the arrow
