#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from bistable_saddle_params import *

I = 3.475

mpl.rcParams.update({'font.size': 20/1.25})

def F(x,s,a):
	return -x + s/(1+np.exp(-(a*(x-s/4))))
def G(x,g_0,a_g,I):
	return g_0/(1+np.exp(-(a_g*(x-I))))-shift

def nullcly(v):
	return G(v,g_0,a_g,I)

def nullclx(v):
	return F(v,s,a)


x_range = np.linspace(-15.,20.,5000)

xy_data = np.load("../data/r_rec_bistable_saddle.npy")

fig_size = (10.,10.)
axis_size = (6.456,4.670)
axis_pos = ((fig_size[0]-axis_size[0])/2.,(fig_size[1]-axis_size[1])/2.)

fig,ax = plt.subplots(1,1,figsize=fig_size)
ax.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))




ax.plot(x_range,nullclx(x_range),c=((31.+(255.-31.)*.5)/255,(119.+(255.-119.)*.5)/255,(180.+(255.-180.)*.5)/255))
ax.plot(x_range,nullcly(x_range),c=((255.+(255.-255.)*.5)/255,(102.+(255.-102.)*.5)/255,(0.+(255.-0.)*.5)/255))

ax.plot(xy_data[:,0],xy_data[:,1],c='k')

ax.set_xlim([-1.,4.])
ax.set_ylim([.25,4.5])

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.savefig("../graphics/spiking_dyn_xy_bistable_saddle.svg")


plt.show()

#import pdb
#pdb.set_trace()


