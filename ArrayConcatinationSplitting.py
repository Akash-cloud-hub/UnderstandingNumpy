import numpy as np
from icecream import ic

x = np.array([1,2,3])
y = np.array([3,2,1])
z = np.array([1,2,3])

ic(np.concatenate([x,y,z]))

d2 = np.array([[1,2,3],
               [12,23,34]])
ic(np.concatenate([d2,d2]))

#concatenate along the second axis
ic(np.concatenate([d2,d2],axis=1))

grid = d2.copy()
#vertically stack the array
ic(np.vstack([x,grid])) # adding a new row
y=np.array([[99],
            [99]])
ic(np.hstack([grid,y])) # adding a new column

