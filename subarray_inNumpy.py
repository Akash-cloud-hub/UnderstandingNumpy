import numpy as np

x2 = np.random.randint(1, 10, size=(9, 9))

print(x2)
x2_sub = x2[:2, :2]
print()

print(x2_sub)

print()
x2_sub[0, 0] = 99
print(x2_sub)
print()
print(x2)

# x2_sub is not a copy of x2 , it's just a sliced part of the original data ,
# so any changes made to x2_sub will affect x2

x2_sub_copy = x2_sub.copy() # this is a copy made ,so now it won't affect the original data
print(x2_sub_copy)
print()
x2_sub_copy[0,0] = 130
print(x2_sub_copy)
print()
print(x2_sub)
print()
print(x2)