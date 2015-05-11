import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy import integrate
import time
from scipy.interpolate import interp1d

def f(x):
    return cos(x/9)*sin(x)**2

def fsing(x):
    return x**(-3/4)


# Before doing integration, it is useful to know the lambda operator

# It is basically a way to define a function when you need one

lamb= lambda x: cos(x/9)*sin(x)**2

print lamb(2)

# This is equivalent to f which we defined above

# We can also call it inside a function

def p(n):
    return lambda x: x+n

pten=p(10)
print pten(5)

# This makes a function once n is specified

# The reason you want this is because some operations take functions as input.  You may not what to define these functions globally, but only when you need them

# Ingration is one such operators


# Most basic option is the function quad from scipy

# 1-dimensional integration with scipy
a=0
b=10
t1 = time.time()
I2=quad(f,a,b)
# Here f is the name of the function and a and b are the limits of integration

print time.time() - t1
#prints 0.00040602684021

print I2
#prints (3.93638587691,6.860665464555882e-12)
#(second term is an error estimate)

# We could have written this same integral as

I2=quad(lambda x: cos(x/9)*sin(x)**2,0,10)
print I2
#prints (3.93638587691,6.860665464555882e-12)

#Just to compare, we can do the same integral made by hand

t1 = time.time()
x=np.linspace(a,b,40)
dx=x[1]-x[0]
y=f(x)*dx
I1=(y[0]+y[-1])/2+sum(y[1:-1])
print time.time() - t1
#prints 8.58306884766e-05

print I1
#prints 3.93845493792

# Accurate to 3 significant figures and runs faster

# Obvious approach isn't as bad as you might think

# Quad will work better on more complciated integrals (especially oscilatory integrals or integrands with singular points)


# One major advantage of quad is infinte integration

Inft=quad(lambda x: np.exp(-x),0,np.infty)
print Inft
#prints (1.0000000000000002, 5.842606742906004e-11)





####How about Multidimensional integration ####

def g(y,x):
    return y*(x+y)**2



I3=integrate.dblquad(g,0,1,lambda x:0,lambda x:1)[0]
print I3
#prints (1.0000000000000002, 5.842606742906004e-11)

#Notice that we used a lambda operator here to create a function.  We could have done a more painful job line this

def g0(x):
    return 0
def g1(x):
    return 1


I4=integrate.dblquad(g,0,1,g0,g1)[0]
print I4

# See how we needed to create the functions ahead of time.  Lambda is nice because we get to create the function when we need it



# Numerical Integration has some options that are useful

print integrate.quad(lambda x: np.cos(1./x),0,10)
#prints error about max subdivisions and returns (8.47930430175785, 0.0014482921907745046) - this is a big error

print integrate.quad(lambda x: np.cos(1./x),0,10,limit=100000)
# limit increases the maximum number of allowed subdivisions.  For highly oscilatory integrals, this is very helpful
#prints (8.47918978494334, 6.350133396892943e-08) which is much more accurate.



### Some challenges with integration ####



def int(x):
    temp = integrate.quad(lambda y: x*np.exp(-x*y),0,np.inf,limlst =5000,limit=5000,epsabs=1.49e-14, epsrel=1.49e-14)[0]
    return temp

# This function is 1 for any x

q=np.logspace(0,10,100)
out=[]
for elem in q:
    out.append(int(elem))

plt.figure()
plt.loglog(q,out)
plt.show()


# We see that we have very good agreement with 1 up to x = 10^5 and then we get 0

# The problem is that the region where we get most of the contribution is 0 to 1/x which is becoming very small


# An easy fix is to split up the integral

def intfix(x):
    temp1 = integrate.quad(lambda y: x*np.exp(-x*y),0,10./x)[0]
    temp2 = integrate.quad(lambda y: x*np.exp(-x*y),10./x,np.inf)[0]
    return temp1+temp2

# For the integrator to evaluate lots of points in the dominant region

q=np.logspace(0,10,100)
out=[]
for elem in q:
    out.append(intfix(elem))

plt.figure()
plt.loglog(q,out)
plt.show()

# Now we get 1 for all values of x


# Another challenges are sigular points

def fsing(x):
    return x**(-3/4)

# This is a sigular function, with a well behaved integral


Ising1=quad(fsing,0.00001,1,limit=5000,epsabs=1.49e-14, epsrel=1.49e-14)[0]


print Ising1
#prints 11.512925465
#The correct answer is 4.


#Just to compare, we can do the same integral made by hand


x=np.linspace(0.00001,1.,39)
dx=x[1]-x[0]
y=fsing(x)*dx
Ising2=(y[0]+y[-1])/2+sum(y[1:-1])
#print time.time() - t1
#prints 8.58306884766e-05

print Ising2
# prints 1319.990445
# We see that quad is doing much better (but neither is doing very well)


##### Interpolation

#There are lots of situations we need to use the same integral over and over again

#instead of recomputing it of every value, just make a table and fit it.  If this functino is smooth, this is often a very good approximation.


def nint(y):
    return integrate.quad(lambda x: np.cos(x),0,y)

t=np.linspace(0,10,100)
nsin=[]
temp=0
for elem in t:
    temp=nint(elem)[0]
    nsin.append(temp)

isin=interp1d(t,nsin)
t=np.linspace(0,10,10000)
diffsin=isin(t)-np.sin(t)
plt.figure()
plt.plot(t,diffsin)
plt.show()
#Error of 10^(-3)


t1 = time.time()
isin(9.21)
print time.time()-t1
#prints 0.000171899795532

t1 = time.time()
nint(9.21)
print time.time()-t1
#prints 7.82012939453e-05

#In this case, numerical integration is a bit faster

# Let's try something harder

def nint2(y):
    return integrate.quad(lambda x: 2*np.cos(x**2)*x,0,y,limit=1000)

t=np.linspace(0,10,1000)
nsin2=[]
temp=0
for elem in t:
    temp=nint2(elem)[0]
    nsin2.append(temp)


isin2=interp1d(t,nsin2)
t=np.linspace(0,10,10000)
diffsin2=isin2(t)-np.sin(t**2)
plt.figure()
plt.plot(t,diffsin2)
plt.show()
#We still have an error of 10^(-3)

t1 = time.time()
isin2(9.21)
print time.time()-t1
#prints 0.00014591217041

t1 = time.time()
nint2(9.21)
print time.time()-t1
#prints 0

#We see that there is almost no change in speed for the interpolator.  The integral now takes 10 times longer



