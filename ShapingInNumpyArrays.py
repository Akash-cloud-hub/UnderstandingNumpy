import numpy as np
from icecream import ic
data = np.array([[10,12],[20,22],[30,32]])

print(data.reshape(2,3))
print()
print(data.reshape(3,2))
print()

arr = np.arange(6)
print(arr)
print()
arr = arr.reshape(2,3)# rows , columns
ic(arr)
arr = arr.transpose()
ic(arr)

newarr = np.arange(1,10).reshape(3,3)
ic(newarr)


arra1 = np.arange(1,4)
ic(arra1)
arra1= arra1.reshape(3,1)
ic(arra1)
arra1= arra1.reshape(1,3)
ic(arra1)

ic(arra1[np.newaxis,:]) # puts it inside another array

ic(arra1[:,np.newaxis])

