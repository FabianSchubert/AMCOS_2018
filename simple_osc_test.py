#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def s(x):
	return np.tanh(x)


def F(x):

	r = np.ndarray((2))

	r[0] = c*s(x[0]) - d*x[0] - x[1] + I
	r[1] = (x[0] + a - b*x[1])/tau

	return r

def f_quiver(x,y):

	return c*s(x) - d*x - y + I,(x + a - b*y)/tau 

def nullcl_x(x):

	return c*s(x) - d*x + I

def nullcl_y(x):

	return (x + a)/b

def step(r,F,dt):

	ra=r+0.5*dt*F(r)
	rb=r+0.5*dt*F(ra)
	rc=r+dt*F(rb)
	return r+(dt/6.)*(F(r)+2.*(F(ra)+F(rb))+F(rc))


T = 100.
dt = 0.1
n_t = int(T/dt)
T = dt*n_t

I = 2.
a = 0.
b = .25
c = 2.
d=0.

tau = .5

x_rec = np.ndarray((n_t,2))

x = np.random.normal(0.,0.1,(2))

for t in tqdm(range(n_t)):

	x = step(x,F,dt)
	x_rec[t,:] = x


x_range = np.linspace(-2.,2.,1000)

X,Y = np.meshgrid(np.linspace(-2.,2.,20),np.linspace(-2.,2.,20),indexing="ij")
VX,VY = f_quiver(X,Y)
plt.quiver(X,Y,VX,VY,scale_units=None)

plt.plot(x_range,nullcl_x(x_range))
plt.plot(x_range,nullcl_y(x_range))

plt.plot(x_rec[:,0],x_rec[:,1])
#plt.scatter(x_rec[:,0],x_rec[:,1],c=np.array(range(n_t)),s=1.)
#plt.quiver(x_rec[:-1,0],x_rec[:-1,1],x_rec[1:,0]-x_rec[:-1,0],x_rec[1:,1]-x_rec[:-1,1],scale_units="xy",angles="xy",scale=1.)
#plt.streamplot(x_rec[:-1,0],x_rec[:-1,1],x_rec[1:,0]-x_rec[:-1,0],x_rec[1:,1]-x_rec[:-1,1])



plt.show()

plt.plot(x_rec[:,0])
plt.show()