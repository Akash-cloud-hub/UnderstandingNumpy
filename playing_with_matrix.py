import numpy as np
x2 = np.array([[10,12],[20,22],[30,32]])
print(x2)
print()
print(x2[0,1])
print()
print(x2[1:])
print()

#column turn into row and row turn into column
x3 = x2[:2,:2].copy()
print(x3)
print()
x4 = np.array([ x3[:,0] , x3[:,1] ])  #[ gets the values of all rows , gets the values of all columns]
print( "transposed ", x4)
print()

x5 = x3.copy().transpose()
print(x5)



print(x2.reshape(2,3))

