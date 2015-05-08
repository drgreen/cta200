import numpy as np
import time
## Main advantage is speed (expand taken from online course)

def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = np.arange(10000000)
    Y = np.arange(10000000)
    Z = X + Y
    return time.time() - t1

print trad_version(), numpy_version()

print time.time()

# The key object is the array

#we can make an array like this

arr1d=np.array([1,2,3,4])
arr2d=np.array([[1,2],[3,4]])

#We can make arbitrarily complicated dimensional arrays this way

#We can access individual elements like we did for a list

print arr1d[1]
#prints 2

#for higher dimension arrays use this structure

print arr2d[0,1],arr2d[1,0]
#prints 2, 3


#There are lots of built in functions that make simple arrays very fast
a=np.arange(0,10)
#makes array([0,1,...,9])

b=np.linspace(0,1,11)
#makes array([0.0,0.1,..,1.]

c=np.logspace(0,5,6)
#makes array[1.,10.,100.,..,1.00e+05]

d=np.zeros(5)
#makes a shaphe (5) array - array([ 0.,  0.,  0.,  0.,  0.])


e=np.zeros((2,3))
#makes a shape (2,3) array

f=np.zeros_like(b)
#makes an array of zeros with the same shape as b

g=np.identity(3)
#makes a 3 by 3 array with structure of 3 by 3 identity matrix
# array([[ 1.,  0.,  0.],[ 0.,  1.,  0.],[ 0.,  0.,  1.]])

# Numpy can also defines a matrix
mtx=np.matrix([[1,2],[3,4]])
print mtx*mtx
#prints matrix([[ 7, 10],[15, 22]])

# A matrix is not the same as a 2 by 2 array
arr=np.array([[1,2],[3,4]])
print arr*arr
#prints array([[ 1,  4],[ 9, 16]]

#We see that d*d is just the square of each element while c*c is matrix multilication

#We can turn an array into matrix?

arrtomtx=np.matrix(arr)

print arrtomtx*arrtomtx
#prints matrix([[ 7, 10],[15, 22]])

#or we can force the array to do matrix operations

print np.dot(arr,arr)
#prints matrix([[ 7, 10],[15, 22]])


# The linear algebra package will let us do anything we want

print np.linalg.det(arr)
#prints -2.

# Most numpy functions work nicely on arrays

# Suppose we want to complute the length of a vector

vec=np.array([1,-2,3])

print np.sqrt((vec*vec).sum())
#prints 3.7416573867739413


## A lot of calculations (data analysis) involve manipulating shape of array

#first we can determine the dimension and shape of an arrage

d=np.array([[1,2],[3,4],[5,6]])

print d.ndim
#prints 2 (2d array)

print d.shape
#prints (3,2)

#this means that d[2,1] exists, but not d[1,2]

#We might want to reshape it

x1d=np.arange(100)
x2d=x1d.reshape((5,20))

#or we might want to flatten it into one long array

xflat=x1d.flatten()

# for example, suppose we want to go through the elemnts one at a time

for elem in x1d:
    print elem

#for shape (a,b) this outputs a arrays of size b

#instead you might one just the individual numbers so

for elem in xflat:
    print elem

#this writes the numbers from 0-99 one at a time

