### Here we want to learn about defining iterative functions

#First we define the factorial.  We want to have Gamma[x] = x Gamma[x-1] and Gamma[1]=1
def reit(n):
  
  if n<=1:
      #If n=0, or any value it can't determine, set to 1
    return 1
  else:
      #If it is greater than one, call again iteratively by definition
    return n*reit(n-1)


print reit(5),reit(3)


# Now lets define a sorting algorithm this way

def mysort(a):
  for n in range(1,len(a)):
    #Read in one element at a time, starting with second (first is sorted)
    value=a[n]
    #set marker for previous
    i=n-1
    while i>=0 and (value < a[i]):
        #if i is not past the first element, but value < previous element swith the two
      a[i+1]=a[i]
      a[i] = value
      #now move the marker one to the left and repeat
      i-=1
#1st element is sorted.  When we get to the nth element, the n-1 previous elements are sorted.  Just need to place it in the right spot

b=[1,5,7,8,1,9,2]
mysort(b)
print b