import sys


# Define a main() function
def main():
    # Get the name from the command line, using 'World' as a fallback.
  
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'World'
    print 'Hello', name
  # To see how things are read in try : print sys.argv


# This is the standard boilerplate that calls the main() function.

if __name__ == '__main__':
    main()

# As a test, we can see what __name__ is when we call hello via hello2
else :
    print __name__
    #when we use hello2, __name__ = 'hello' when we load hello.py

