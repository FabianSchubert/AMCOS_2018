#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 20/1.25})

def F(x,s,a):
	return -x + s/(1+np.exp(-(a*(x-s/4))))
def G(x,g_0,a_g,I):
	return g_0/(1+np.exp(-(a_g*(x-I))))-shift

def nullcly(v):
	return G(v,g_0,a_g,I)

def nullclx(v):
	return F(v,s,a)


x_range = np.linspace(-10.,20.,5000)


fig_size = (10.,10.)
axis_size = (6.456,4.670)
axis_pos = ((fig_size[0]-axis_size[0])/2.,(fig_size[1]-axis_size[1])/2.)

fig,ax = plt.subplots(1,1,figsize=fig_size)
ax.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))

s=10*2**0.5
a=.3
g_0=200.
a_g=2
I = 7.
shift=.0

ax.plot(x_range,nullclx(x_range),c=((31.+(255.-31.)*.5)/255,(119.+(255.-119.)*.5)/255,(180.+(255.-180.)*.5)/255))


s=10*2**0.5
a=1.85
g_0=200.
a_g=2
I = 7.
shift=.0

ax.plot(x_range,nullclx(x_range),c=(31./255,119./255,180./255))



s=10*2**0.5
a=1.85
g_0=200.
a_g=2
I = 6.
shift=1.5

ax.plot(x_range,nullcly(x_range),c=((255.+(255.-255.)*.5)/255,(102.+(255.-102.)*.5)/255,(0.+(255.-0.)*.5)/255))

s=10*2**0.5
a=1.85
g_0=20.
a_g=.5
I = 6.
shift=5.

ax.plot(x_range,nullcly(x_range),c=((255.+(255.-255.)*.0)/255,(102.+(255.-102.)*.0)/255,(0.+(255.-0.)*.0)/255))

ax.set_xlim([-5.,12.])
ax.set_ylim([-2.,9.])

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.savefig("nullcl_illstr.svg")


plt.show()


