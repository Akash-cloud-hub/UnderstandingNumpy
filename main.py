import numpy as np

my_list = [132, 150, 120, 70, 89, 90]
a = np.array(my_list)

print(a)
print()

zero_array = np.zeros(2)
one_array = np.ones(2)
print(zero_array)
print()
print(one_array)
print()

ordered_numbers = np.arange(100)
print(ordered_numbers)
print()

even_spacing = np.arange(0 , 101 , 2) # goes from 0 to 101 with a spacing of 2 numbers in between
print(even_spacing)

print(np.linspace(0,10,num = 7)) # evenly distributes 0-10 and get every multiple of 1/7 till 10

print()
print(a)
print()
print(a[0])
print(a[3])
print(a[4])
print(a[len(a)-1])
print(a[-1])# access last value of list
print(a[-2])

x2_list=[
    [123,100,200],
    [4013,6690,901],
    [13213 , 8371 , 9983]]

x2 = np.array(x2_list)

print(x2[1][0])
print(x2[1,0])

print(x2[2,1])
print(x2[1,-1])
print(x2[0,0])
x2[0,0] = 200.50
print(x2)

x3 = np.array([1,2,3,4,5,6,7,8,9,10])

print(x3[1:5])
print(x3[1:])
print(x3[2:])
print(x3[-2:])
print(x3[::2])
print(x3[::3]) # takes the indexes from the multiples of 3
print()
print(x3[1::2]) # takes the indexes from the multiples of 2 with a given starting index of 1
print(x3[1::3]) # takes the indexes from the multiples of 3 with a given starting index of 1
print()
print(x3[::-1]) # takes values in reverse in steps of -1
print(x3[5::-1])