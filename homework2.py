import numpy as np

array=np.array([[0,1,2],[10,11,12],[20,21,22],[30,31,32]])
print(array)

#accessing 3rd row and 2nd column
print(array[2,1])

#Accessing rows alternatively
print(array[0:3:2,0:3])

#Reversing the order of rows
print(array[4::-1,0:3])

#creating a new 2D array with arrange 4 by 4, 1 to 16 numbers

new_array = np.arange(1,17)
new_array1 = new_array.reshape(4,4)
print(new_array1)
print(new_array1.max())
print(new_array1.min())