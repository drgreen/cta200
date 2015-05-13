from sage.all import *

#This is a sage file where we will test out a few options

#Call this as a sage file as sage snb.sage

#Let's start with algebra

#Depending on how you run sage, you may need to define variables, functions, etc.
x,y = var('x,y')

#Sage also has built in constants

sin(pi)
#0
e^(2*pi*I)
#1

# Now suppose that you have two other quantities defined in terms of x,y
p=(x+y)^4
q=x^2+ 15*y+4*x*y^2

# Now I want to expand something written as a function of p and q in terms of x and y

ouput=(p+q).expand().full_simplify()
print output
#prints x^4 + 4*x^3*y + 6*x^2*y^2 + 4*x*y^3 + y^4 + 4*x*y^2 + x^2 + 15*y


# Sage will only give numeric answers if you tell it

cos(x).substitute(x=1)
#cos(1)

cos(x).substitute(x=1).n()
#0.540302305868140

# We can solve algebriac equations

sol = solve(a*x^2+b*x+c==0,x)
print sol
# [x == -1/2*(b + sqrt(b^2 - 4*a*c))/a, x == -1/2*(b - sqrt(b^2 - 4*a*c))/a]

#A good thing to do is to make a solutions dictionary so you can use it later
eqn=x^2+2*x*y+14==0
sols=solve(eqn,x,solution_dict=True)
#[{x: -y - sqrt(y^2 - 14)}, {x: -y + sqrt(y^2 - 14)}]

# now to use the first solution
sol1=sols[0][x]
#-y - sqrt(y^2 - 14)

# Now plug it into the next equation

eqn2=10*x^2+15*y+y^2
eqn2.substitute(x=sol1).full_simplify()
#21*y^2 + 20*sqrt(y^2 - 14)*y + 15*y - 140

### Differentiation

#take a derivative

u = var('u')
diff(sin(u), u)
#cos(u)

#or we can write

x, y = var('x,y')
f = x^2 + 17*y^2
f.diff(x)
#2*x
f.diff(y)
#34*y

# Also very useful is Taylor series

f=cos(x)
f.taylor(x,0,4)
#1/24*x^4 - 1/2*x^2 + 1

#or something a bit more complicated

f=(cos(x)-sin(x))/x^3
f.taylor(x,0,0)
#-1/2/x - 1/x^2 + 1/x^3 + 1/6

# This is really helpful when there are cancelations

f=(x*cos(x)-sin(x))/x^3
f.taylor(x,0,2)
# 1/30*x^2 - 1/3

# We can also expand around infinity
f=(x+1)/x^3
f.taylor(x,infinity,2)

# The expansion around infinity doesn't seem as powerful as in mathematica. Gives an error if we use cos(x) /x (but might work if we give it more information)


# Differential Equations
t = var('t')
r = function('r',t)
DE = diff(r, t) + r - 1
desolve(DE, [r,t])
#(_C + e^t)*e^(-t)

#We can do something more complicated, but we need to be careful about assumptions

a,b = var('a,b')

assume(4*b>a^2)
# We need this assumption, otherwise it gives an error


t = var('t')    # define a variable t
r= function('r',t)   # define x to be a function of that variable
DE2 = diff(r, t,t)+a*diff(r,t)+b*r
dsol=desolve(DE2, [r,t])
#(_K2*cos(1/2*sqrt(-a^2 + 4*b)*t) + _K1*sin(1/2*sqrt(-a^2 + 4*b)*t))*e^(-1/2*a*t)

# The assumption was so that it knew how to define the square root

#We can plug in specific constants like this
dsol.substitute(_K1=1,_K2=1)
#(cos(1/2*sqrt(-a^2 + 4*b)*t) + sin(1/2*sqrt(-a^2 + 4*b)*t))*e^(-1/2*a*t)


## Integration ##

# Indefinite integral

integral(x*sin(x^2), x)
#-1/2*cos(x^2)

#Definite Integrals
integral(x*sin(x)*cos(3*x)^2,x,0,1)
# -1/28*cos(7) + 1/20*cos(5) - 1/2*cos(1) + 1/196*sin(7) - 1/100*sin(5) + 1/2*sin(1)

#we probably want to give the numeric value
integral(x*sin(x)*cos(3*x)^2,x,0,1).n()
#0.150783583419853

#numeric integration
numerical_integral(x*sin(x)*cos(3*x)^2,0,1)
#(0.15078358341985298, 1.6740340604820879e-15)

#This is most likely using quad

# But we can even use our python commands in sage

from scipy.integrate import quad
quad(lambda x:x*sin(x)*cos(3*x)^2,0,1)
#(0.150783583419853, 1.6740340604820882e-15)


#Linear algebra

#Define a matrix

M=matrix(3, 3, [x,0,2*y, 0,y*x,0,2*y,0,x])
#[  x   0 2*y]
#[  0 x*y   0]
#[2*y   0   x]

# Perform basic operators

det(M)
# x^3*y - 4*x*y^3


