import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.,1.,100)
y=x**2

#Basic plot of a curve
plt.figure()
plt.plot(x,y)
plt.show()

#same curve on a log log plot
plt.figure()
plt.yscale('log')
plt.xscale('log')
plt.plot(x,y)
plt.show()


# scatter versus plot
plt.figure()
plt.scatter(x,y)
plt.show()



# barchat versus plot fix xrange
plt.figure()
plt.bar(x,y,0.01)
plt.xlim(0.,1.)
#plt.show()
plt.savefig('bar.pdf', format='pdf')
plt.close()
