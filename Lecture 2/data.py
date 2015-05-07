# Here I want to explore different data structures

# The basic data types are usually, int, float, string, complex

# Python decides which one is which when you define a variable

# This is an integer

integer=2

# This is a floating point number

floating = 2.

# This is a string

string = '2'

# This might seem important, but here is the difference

print 'This is integer division :' +str(1/integer)

print 'This is float division :' + str(1/floating)

# This ouputs 0 and 0.5.  We need to keep track.

# We also see that we need to convert types.  To output a string + number we needed to convert using str()

# We can also convert integers to float or vise versa

print 'We can make integer division float : ' + str(1/float(integer))

#prints 0.5

#Finally, there are complex numbers

z=3+1j

print z*z

#We can also make a complex number this way

z=complex(3,1)

print z*z, z


# These basic objects can then be stored as elements of larger objects

# The most basic object is a list

# A list takes the form a = [entry1,..,entryN].  All entries are the same data types.

# Here is an example

a = [10,9,4,2,1,9]

# We can then use specific entries by writing a[], starting from 0

print a[0]

#prints 10

# From this list, we can also pick out specific sublists
#Print sublist of elements 0, 1
print a[:2]
#prints [10,9]

# We can write it the same way with the 0
print a[0:2]
#prints [10,9]

#prints elems 3 to the end
print a[3:]
#prints [2,1,9]

#Prints element 4
print a[4:5]
#prints [1]

#prints beginning to end -1 (second to last)
print a[:-1]
#prints [10, 9, 4, 2, 1]


# A very important feature is being able to add or remove elements

# To add an element at the end
a.append(0)
print a
#prints [10, 9, 4, 2, 1, 9, 0]

# Add a new number in position 1 (between 10 and 9)
a.insert(1,0)
print a
#prints [10, 0, 9, 4, 2, 1, 9, 0]

#To remove that point, we can use pop or remove
a.pop(1)
print a
#prints [10, 9, 4, 2, 1, 9, 0]

#If we know the value we want to remove the first instance this way
a.remove(9)
print a
#prints [10, 4, 2, 1, 9, 0] - notice it only removed the first 9


# for loops are easy ways to interate through a list

for elem in a:
    print elem

# This doesn't have to be numbers, it works for any data type

animals=['ducks', 'cows','chickens']

for thing in animals:
    print 'I like '+thing



# A dictionary is a more
b={}
b['dogs']=5
b['cats']=10
print b
#prints {'dogs': 5, 'cats': 10}

# We can also define it from the beginning with this structure
c={'dogs': 5, 'cats': 10}
print c
#prints {'dogs': 5, 'cats': 10}

#but we can add a new entry to our dictionary anytime
c['cows']=0
print c
#prints {'cows': 0, 'cats': 10, 'dogs': 5}

# 'cows', 'cats' and 'dogs' are the keys
# 0, 10, 5 are the values

# we can make a list of either one in the following way
print c.keys()
#prints ['cows', 'cats', 'dogs']

print c.values()
#prints [0, 10, 5]

#So we can cycle through them with a for loop

for key in c.keys():
    print 'There are ' + str(c[key]) + ' ' + key

#prints There are 0 cows /n There are 10 cats /n There are 5 dogs