#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def F(x,s,a):
	return -x + s/(1+np.exp(-(a*(x-s/4))))
def G(x,g_0,a_g,I):
	return g_0/(1+np.exp(-(a_g*(x-I))))-shift

def nullcly(v,g_0,a_g,I):
	return G(v,g_0,a_g,I)

def nullclx(v,s,a):
	return F(v,s,a)

s=10*2**0.5
a=1.85
g_0=400.
a_g=2.
shift=1.3
T_x=.25
T_y=25.
I=0.

import pdb

x_lims = [-5.,10.]
y_lims = [-5.,15.]

fig, ax = plt.subplots(1,1)
ax.set_position([0.1, 0.2, 0.8, 0.7])
ax.axis([x_lims[0],x_lims[1],y_lims[0],y_lims[1]])
axI = plt.axes([0.1, 0.1, 0.8, 0.03])
sI = Slider(axI,"I",0.,20.)




x_res_nullcl = 2000
x_res_grid = 50
y_res_grid = 50

x_range_mesh = np.linspace(x_lims[0],x_lims[1],x_res_grid)
y_range_mesh = np.linspace(x_lims[0],x_lims[1],y_res_grid)
X,Y = np.meshgrid(x_range_mesh,y_range_mesh,indexing="xy")
VX = F(X,s,a) - Y
VY = G(X,g_0,a_g,I) - Y

x_range_nullcl = np.linspace(x_lims[0],x_lims[1],x_res_nullcl)

l_nullcl_x, = ax.plot(x_range_nullcl,nullclx(x_range_nullcl,s,a))
l_nullcl_y, = ax.plot(x_range_nullcl,nullcly(x_range_nullcl,g_0,a_g,I))
#stream = ax.streamplot(x_range_mesh,y_range_mesh,VX,VY)

pdb.set_trace()

def update_I(val):
	global I
	global stream

	I = val
	l_nullcl_y.set_ydata(nullcly(x_range_nullcl,g_0,a_g,I))
	VX = F(X,s,a) - Y
	VY = G(X,g_0,a_g,I) - Y

	#stream.arrows.remove()

	#stream = ax.streamplot(x_range_mesh,y_range_mesh,VX,VY)

sI.on_changed(update_I)

plt.show()