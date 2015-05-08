import numpy as np
import math as m
from pylab import *

#Example - suppose I want to store an 2d electric field E_(x,y) on a grid of points (x,y) that run from 0 to L_x and 0 to L_y
pi=m.pi
Lx=1.
Ly=2.
n=25


# For making figures, it is often useful to make a meshgrid

x,y=np.meshgrid(Lx*np.linspace(0,Lx,n,endpoint=True),Ly*np.linspace(0,Ly,n,endpoint=True))

# A meshgrid will create an array such that for every pair of integer i,j between 0, n-1 we can get the x and y coordinate

# i.e. x[i,j] and y[i,j] are the values for some point i, j

# this is non-trivial, because we want x(y) to vary as we change j (i)

# We can see this structure as follows

print x[0,0], x[0,1],x[0,2]
#prints 0.0 0.0416666666667 0.0833333333333

print y[0,0], y[0,1], y[0,2]
#prints 0.0 0.0 0.0

# Now let's make an electric field for every point
Ex=5*np.sin(2.*pi*x/ Lx)*np.cos(2.*pi*y/Ly)
Ey=10.*np.sin(2.*pi*y/Ly)

#Notice the advantage of NOT using matrix multiplication.  We can define the whole arrage of E_x and E_y using only multiplication and standard functions


# Now let's plot the electric field

figure()
quiver(x, y, Ex, Ey, units='width')
show()

# Meshgrid is also very useful for contours plots

