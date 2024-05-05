import numpy as np
x1 = np.random.randint(1,10,size=6)
x2 = np.random.randint(1,10,size=(9,9))
x3 = np.random.randint(1,10,size=(6,3,3))

print(x1)
print()
print(x2)
print()
print(x3)
print()
print()
print()
#accessing top 2 rows and 3 columns
print(x2[:2,:3])
print()

# accessing all rows and every other
print(x2[0:,0::2])
print()

# access reverse
print(x2)
print()
print()
print(x2[::-1,::-1]) # I used the range function to go backwards for each column and row .

#access first column of x2
print()
print(x2)
print()
print(x2[:,0])

# access first row of x2
print()
print(x2)
print()
print(x2[0])

