import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, rgamma

# The area of a circle of radius 1 is \pi

# We can compute this as an integral using monte carlo

def area(n):
    count = 0
    farea=[]
    for j in xrange(n):
        #sample x,y from -1 to 1
        x = 2.* random.random()-1.
        y =  2.* random.random()-1.
        if x**2+y**2<=1:
            count += 1.
        #only add the result if it is inside the cicle
        if j%100 ==0 and j!=0:
            farea.append(np.abs(4*float(count)/float(j)-np.pi))

    return farea

# Monte Carlo result is give as 4 times number of accepted points / n


tarea=area(100000)
Num=np.arange(100,100000,step=100)

plt.figure()
plt.plot(Num,tarea)
plt.xscale('log')
plt.yscale('log')
plt.show()


# Now lets consider the d-ball which has volume pi^(d/2) / Gamma(d/2+1)

# E.g. lets try 6-d ball

def dvol(n,d):
    analytic=np.pi**(float(d)/2.)*rgamma(float(d)/2.+1)
    count = 0
    Narea=[]
    x=np.zeros(d)
    for j in xrange(n):
        #sample x_i from -1 to 1
        for i in xrange(d):
            x[i]=2.* random.random()-1.
        if (x*x).sum()<=1:
            count += 1.
        #only add the result if it is inside the cicle
        if j%100 ==0 and j!=0:
            Narea.append(np.abs(2**(d)*float(count)/float(j)-analytic))
    
    return Narea

vol6=dvol(10000,6)
Num=np.arange(100,10000,step=100)

plt.figure()
plt.plot(Num,vol6)
plt.xscale('log')
plt.yscale('log')
plt.show()



# Now let's try the same thing with importance sampling

# We are going to pick from a gaussian distribution with some variance
def gaussvol(n,d,sigma):
    analytic=np.pi**(float(d)/2.)*rgamma(float(d)/2.+1)
    count = 0
    Narea=[]
    x=np.zeros(d)
    for j in xrange(n):
        random.seed()
        #sample x_i from -1 to 1
        for i in xrange(d):
            x[i]=random.gauss(0,sigma)
        
        
        if (x*x).sum()<=1:
            # Here we use importance sampling to weight the result
            count += np.sqrt(2*np.pi*sigma**2)**(d)*np.exp((x*x).sum()/(2.*sigma**2))
        #only add the result if it is inside the cicle
        if j%100 ==0 and j!=0:
            Narea.append(np.abs(float(count)/float(j)-analytic))
    
    return Narea

# Lets try a bunch of values of sigma to see how it works
npoints=100000
dim=6
vol6high=gaussvol(npoints,dim,5.)
vol6low=gaussvol(npoints,dim,0.1)
vol6s1=gaussvol(npoints,dim,1.)
vol6s2=gaussvol(npoints,dim,0.5)
vol6s3=gaussvol(npoints,dim,0.333)
vol6s4=gaussvol(npoints,dim,0.25)
vol6s5=gaussvol(npoints,dim,0.2)
vol6flat=dvol(npoints,dim)
Num=np.arange(100,npoints,step=100)

plt.figure()
plt.plot(Num,vol6s1,c='red')
#plt.plot(Num,vol6s2,c='blue')
plt.plot(Num,vol6s3,c='green')
#plt.plot(Num,vol6s4,c='purple')
plt.plot(Num,vol6s5,c='orange')
plt.plot(Num,vol6high,c='pink')
plt.plot(Num,vol6low,c='black')
#plt.plot(Num,vol6flat,c='black',linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.savefig('limits.pdf',format='pdf', dpi=360)

plt.figure()
plt.plot(Num,vol6s1,c='red')
plt.plot(Num,vol6s2,c='blue')
plt.plot(Num,vol6s3,c='green')
plt.plot(Num,vol6s4,c='purple')
plt.plot(Num,vol6s5,c='orange')
#plt.plot(Num,vol6high,c='pink')
#plt.plot(Num,vol6low,c='black')
plt.plot(Num,vol6flat,c='black')
plt.xscale('log')
plt.yscale('log')
plt.savefig('comparison.pdf',format='pdf', dpi=360)