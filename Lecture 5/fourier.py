import numpy as np
from numpy.fft import fft, fftfreq, ifft, fftshift, fftn
import matplotlib.pyplot as plt

pi=np.pi

#Let's just make sure this works
time=np.arange(0.,2*pi,step=0.1)

testsig=np.exp(complex(0,1)*2*time)
#put in a pure frequency

#Compute fft
ffttest= fft(testsig)

#determine frequencies
freqtest= fftfreq(testsig.size, d=0.1)

plt.figure()
plt.plot(freqtest*2*pi,np.abs(ffttest))
#We rescale the frequency to be an angular frequency
plt.xlim(0, 5)
plt.show()

#Shows a single peak at omega = 2

# Now let's try a gaussian

spacing=0.001

t = np.arange(-10,10,step=spacing)

signal = np.exp(-t**2/2.)/np.sqrt(2*pi)
# This is a gaussian with variance 1 in real time

ft= fft(signal)
#This is the 1d discrete fourier transform

freq = fftfreq(signal.size, d=spacing)
#This is the array of frequencies

print freq[0:5],freq[-5:]
#prints [ 0.    0.05  0.1   0.15  0.2 ] [-0.25 -0.2  -0.15 -0.1  -0.05]

#notice that it starts from 0, goes to + nyquist and then goes -nyquist to 0

# nyquist = 1/2 * 1/spacing = 500


sfreq=fftshift(freq)
sft=fftshift(ft)
#fftshifts just changes to binning so that it runs from -nyquist to + nyquist

print sfreq[0:5],sfreq[-5:]
#prints [-500.   -499.95 -499.9  -499.85 -499.8 ] [ 499.75  499.8   499.85  499.9  499.95]

# Now we can also check that we need to scale both the amplitude of the fft and the frequency to reproduce the gaussian with variance = 1.

plt.figure()
plt.plot(sfreq*(2*pi), np.absolute(sft)*spacing/np.sqrt(2*pi))
#We need to work in angular frequencies.  We also need to rescale our fft by the spacing
plt.plot(t,signal)
plt.xlim(-4, 4)
plt.show()


#  Higher dimensional FFTs

# Time series is naturally a 1d fourier transform.  Images are naturally 2d (or 3d)

x,y = np.meshgrid(np.arange(-1,1,step=0.1),np.arange(-1,1,step=0.1))
signal2d= np.exp(complex(0,1)*5*(x+y))

fft2d=fftshift(fftn(signal2d))
#Getting the 2d (or N-d) fourier transform is essentially identical to 1d

kx_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[0], d=0.1))
ky_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[1], d=0.1))
kx, ky = np.meshgrid(kx_vec,ky_vec)
#Getting the momentum vectors is a bit more work, but not too bad


plt.figure()
plt.pcolormesh(kx,ky,np.abs(fft2d))
plt.axis([0,10,0,10])
plt.colorbar()
plt.show()

# Contour plots doesn't show clear peak at 5 as you could expect

print kx[0,10:15]
# prints [  0.           3.14159265   6.28318531   9.42477796  12.56637061]
# We aren't sampling the frequency we put in because we picked the interval -1,1.


# To see this, repeat with a nicer integral of 0, 2*pi for x and y
x,y = np.meshgrid(np.arange(0,2*pi,step=0.1),np.arange(0,2*pi,step=0.1))
signal2d= np.exp(complex(0,1)*5*(x+y))

fft2d=fftshift(fftn(signal2d))

kx_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[0], d=0.1))
ky_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[1], d=0.1))
kx, ky = np.meshgrid(kx_vec,ky_vec)

print kx[0,31:40]
# prints [ 0.          0.997331    1.994662    2.991993    3.989324    4.98665501 5.98398601  6.98131701  7.97864801]
# Now we are sampling the integer frequencies very well

plt.figure()
plt.pcolormesh(kx,ky,np.abs(fft2d))
plt.axis([0,10,0,10])
plt.colorbar()
plt.show()

# Now we get the peak we want.

#The image is still low resolution.  We fix this with long time integration

x,y = np.meshgrid(np.arange(0,10*2*pi,step=0.1),np.arange(0,10*2*pi,step=0.1))
# Ten times longer integration

signal2d= np.exp(complex(0,1)*5*(x+y))

fft2d=fftshift(fftn(signal2d))

kx_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[0], d=0.1))
ky_vec = 2.0*pi*fftshift(fftfreq(fft2d.shape[1], d=0.1))
kx, ky = np.meshgrid(kx_vec,ky_vec)

print kx[0,314:320]
# prints [ 0.          0.09989166  0.19978332  0.29967497  0.39956663  0.49945829]

#Spacing between k-bins now 0.1 instead of 1.

plt.figure()
plt.pcolormesh(kx,ky,np.abs(fft2d))
plt.axis([0,10,0,10])
plt.colorbar()
plt.show()

# By increasing the length, we get smaller spacing between k-bins and hence higher resolution.  Now we get a very sharp peak at k_x = k_y = 5