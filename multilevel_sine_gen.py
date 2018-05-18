#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from math import sin,sqrt,pi
from mpl_toolkits.mplot3d import axes3d
import scipy as sp


def SPWM(vo,vc):
	vi = []
	voltage = 0
	last = 0
	for i in range(0,len(vc)):
		if vc[i] > 0 and vc[i] < voltage: voltage = vc[i]
		if vc[i] < 0 and vc[i] > voltage: voltage = vc[i]
	sign = 0
	for i in range(0,len(vo)):
		last_sign = sign
		if vo[i] > vc[i]: sign = 1
		if vo[i] <= vc[i]: sign = 0
		if last_sign != sign:
			if voltage == 0: voltage = 1
			else: voltage = 0 
		vi.append(voltage)			
	return np.array(vi)

def recursiveSPWM(m,fc,t,vo):
	t = np.linspace(0,0.02,1000)
	f = 5000
	triangle = (1.0/(m-1))*np.abs(signal.sawtooth(np.pi*fc*t))
	temp = SPWM(vo,triangle)/(m-1)
	for i in range(0,int(m-1)): temp = SPWM(vo,triangle+temp)/(m-1)+temp
	return temp
	
NUMBER_OF_POSITIVE_MINUS_ONE = 19
t = np.linspace(0,0.01,1000)
fc = 5000
vo = np.sin(2*np.pi*50*t)
vi = recursiveSPWM(NUMBER_OF_POSITIVE_MINUS_ONE,fc,t,vo)

vi2 = []
t2 = np.linspace(0,0.02,2000)
for i in range(0,int(len(vi))):
	vi2.append(vi[i])
for i in range(0,int(len(vi))):
	vi2.append(-vi[i])

for i in np.linspace(-(NUMBER_OF_POSITIVE_MINUS_ONE-1),NUMBER_OF_POSITIVE_MINUS_ONE-2,2*(NUMBER_OF_POSITIVE_MINUS_ONE-1)):
	plt.plot(t2,(1.0/(NUMBER_OF_POSITIVE_MINUS_ONE-1))*np.abs(signal.sawtooth(np.pi*fc*t2))+i*(1.0/(NUMBER_OF_POSITIVE_MINUS_ONE-1)),alpha=0.3,color='k')

plt.plot(t2,vi2)
plt.plot(t,vo)
plt.show()

# [ FFT parameters ] #

Fs = 1000

t = np.linspace(0,0.01,Fs)
vo = np.sin(2*np.pi*50*t)
samples = len(t)
T = samples/Fs
k = sp.arange(samples)
freq = k/T
freq = freq[range(int(samples/2))]

# [ 3D plot ] #

F = [500*i for i in range(1,40)]
M = [i for i in range(2,10)]
x,y = np.meshgrid(F,M)
Z = [F for i in range(0,len(M))]
z = np.asarray(Z, dtype=float)

samples = 2*samples
for f in range(0,len(F)):
	for m in range(0,len(M)):
		vi = recursiveSPWM(M[m],F[f],t,vo)
		for i in range(0,int(len(vi))): vi2.append(vi[i])
		for i in range(0,int(len(vi))): vi2.append(-vi[i])
		FFT = sp.fft(vi2)/samples
		FFT = abs(FFT[range(int(samples/2))])
		power_harmonics = FFT**2
		power_fundamental = np.max(power_harmonics)
		temp = 0
		for i in power_harmonics: temp += i
		sol = temp
		z[m,f] = sqrt((sol-power_fundamental)/power_fundamental)

plt.show()

# [ Plots ] #

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride = 2, cstride = 50, color = '#000080', alpha = 0.2) # Surface
plt.show()
















