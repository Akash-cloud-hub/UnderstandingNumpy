"""
Data visualization is representation of data with visual diagrams or graphs such as pi chart , bar graph , line graph and etc.
this method is mainly use to spot patters and changes in data and to draw a conclusion based on the graph .
It's way more efficient than reading the data as reading data makes no sense .
Data visualization allows you to visually compare and contrast data helping you draw valid conclusions and hypothesis."""

import numpy as np
import random

array = np.random.randint(1,100,size=(3,3))
print(array)

print(array.shape)
print(array.ndim)
print(array.size)

print(array[1,2])

new_array = np.random.randint(21,41,size=(20))
print(new_array)
print(new_array[1:8])
