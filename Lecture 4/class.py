### Define a class
import numpy as np

# A class is basically like a function but with a lot more power

# It can store information and can perform multiple functions

# The idea is that we will define something with attributes that we can use to call functions

# e.g.

class Shape:
    # There is a special function that defines the basic object called __init__
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.description = '' # to be defined later
        self.author = ''    # to be defined later

    # Once we have initialize a class, we can define operations
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y

    # We should also define functions that change the attributes
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

#Now we create a specific instance of "Shape"
rec=Shape(10,15)

# We can compute stuff
print rec.area()
#prints 150

#or change properties
rec.describe('hello')
print rec.description
#prints hello

#You need to give each instance a name so it can store its properties
print Shape(11,11).area()
#prints 121 so it can do this

Shape(11,11).describe('hello')
print Shape(11,11).description
#prints '' - it doesn't remember what was done

#Another example
class experiment:
    #We don't need to load informatino when we define a object in the class
    def __init__(self):
        self.noise=1.0
        self.signal=0.0
    def loglike(self):
        return self.signal**2/(2*self.noise**2)
    # We do have to create functions so that we can define the class
    def setnoise(self,text):
        self.noise=text
    def setsignal(self,text):
        self.signal=text

r=experiment()
print r.loglike()
r.setnoise(0.1)
r.setsignal(1.0)
print r.loglike(), r.noise

#We can make it more complicated as well
class experiment2:
    def __init__(self):
        self.noise=1.0
        #Now we will allow for the data to be an array
        self.data=np.array([0])
    def loglike(self):
        return ((self.data*self.data).sum())/(2*self.noise**2)
    def setnoise(self,text):
        self.noise=text
    def setdata(self,text):
        self.data=text


c=experiment2()
print c.loglike()
c.setnoise(0.1)

data=np.array([1,2,3,2,1,2,1])
c.setdata(data)
print c.loglike(), c.noise
