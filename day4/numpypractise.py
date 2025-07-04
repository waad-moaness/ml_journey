import numpy as np 

a= np.array([1,2,3],dtype='int8') # use dtype to change the type or like here use a smaller size for the integer 

# get dimention 
print(a.ndim)

#get shape 
print(a.shape)

#get type 
print(a.dtype)

# get number of elements 
print(a.size)

# the memory size that each element takes in bytes 
print(a.itemsize)

#get total size of the array in bytes 
print(a.nbytes)

# to get a specific row in a multi dimentional arrays us ex a[r , : ]  : means all the columns here

# all nums matrex  
print(np.zeros((2,3,3))) # takes the shape wither it the numger of items or complecx multi d shapes like here 
print( np.ones(7))
print(np.full( (2,2) , 99)) # any other mumber full(shape,number)
# to use a shape of an allready existing arrar 
print(np.full_like(a,5)) 

# random dicimal numbers 
print(np.random.rand(4,3))
#to pass a shape
print(np.random.random_sample(a.shape))

# random integer numbers (start,end, shape) if i didn't add a start it will start from zero 
print(np.random.randint(7, size=(2,2)))
np.identity(5)

