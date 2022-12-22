import numpy as np
#Create a null vector of size 10 but the fifth value which is 1.
x=np.zeros(10) 
x[4]=1 
print(x)

#Create a vector with values ranging from 10 to 49.

num = np.arange(10,40)
print(num)

#Create a 3x3 matrix with values ranging from 0 to 8
x =  np.arange(0, 9).reshape(3,3)
print(x)

#Find indices of non-zero elements from [1,2,0,0,4,0]
x = np.array([1,2,0,0,4,0])
non_zero = np.nonzero(x)
print(non_zero)

#Create a 10x10 array with random values and find the minimum and maximum values.
x = np.random.random((10,10))
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)

#Create a random vector of size 30 and find the mean value.
x = np.random.random(30)
print(x)
z = x.mean()
print(z)




