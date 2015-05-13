

from scipy import fftpack
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from scipy.optimize import fsolve




#define function
def r(eps1,cs):
  temp=(1.+2.*eps1)
  test1=16*eps1*cs**(temp)
  return test1


# We want to make a 2d contour plot of r as a function of both its arguements


n=60
#sample the variables
eps1=np.logspace(-2.,0,n)
cs=np.linspace(0.055,0.15,n)
#make meshgrid for figures x and y variables
xv,yv=np.meshgrid(eps1, cs)

# evaluate the values of r at every point on the grid
rgrid=r(xv,yv)

#make a dictionary that contains the contours we want to label
labels1={0.:'', 0.13: r'$r =0.13$'}
# Here r'$r=0.13$' means to use laTex to write the input (the first r means "raw input")


# make an array of contour levels we want to show
levels = py.arange(0.05, 0.28, 0.02)

#choose color maps)
Rcmap = plt.get_cmap('Blues')

plt.figure(figsize=(8,6),dpi=360)
ax=plt.subplot(1,1,1)
plt.subplots_adjust(bottom=0.3,left=0.3)

# These are important for getting labels in latex
plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif','serif':['Helvetica']})

# Now we plot the contours

#set the x range of the plot
plt.xlim(0.02,1.9)

#set it to be a log x-axis plot
plt.xscale('log')

# Plot the filled contours and save the name of the contours as Crcont
Crcont=plt.contourf(xv,yv,rgrid,levels,cmap=Rcmap)

#plot and label single contour - no fill
Cr=plt.contour(xv,yv,rgrid, [0.,0.13], colors='black', linewidth=1.5,linestyles='dashed')

# Now label those contours - notice we didn't give a name to 0: '' because we used 0 to define the contour in Cr (i.e. we plotted the region between 0 and 0.13)
plt.clabel(Cr, [0.13], inline=1, fmt=labels1,fontsize=14)

#add axis labels
xlab=plt.xlabel(r'$\varepsilon_1$',size=22,labelpad=7)
ylab=plt.ylabel(r'$c_s$',size=22,rotation=0,labelpad=10)
#Rotation for the y-axis default is 90 degrees.
#labelpad gives extra space between axis and label.  We need this because we are going to have lables for the tickmarks as well

ax.set_xticks([0.02,0.1,0.5])
ax.set_xticklabels(['0.02','0.1','0.5'])

#set the size of the tick marks

# There are both big and small ticks (called major and minor) to choose

plt.tick_params(width=0.9,length=6, which='major',labelsize=18,pad=10)
#pad here gives extra extra space between the axis and the labels

plt.tick_params(width=0.75,length=3, which='minor')

# Now make the color bar
cbar=plt.colorbar(Crcont)

# Now set the label of the colorbar - again pad gives this some extra space
cbar.ax.set_ylabel(r'$r$',rotation=0,size=22,labelpad=10)

plt.tight_layout()
#This means it doesn't leave a large white space around the edge

#save
plt.savefig('rcs.pdf',format='pdf', dpi=360)
plt.close()
