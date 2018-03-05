#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 20/1.25})

u = np.load("rate_dyn_u.npy")
I = np.load("I_ext_rate_dyn.npy")
t = np.load("t_axis.npy")

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

fig_size = (10.,10.)
axis_size = (6.456,4.670)
axis_pos = ((fig_size[0]-axis_size[0])/2.,(fig_size[1]-axis_size[1])/2.)

fig,ax1 = plt.subplots(1,1,figsize=fig_size)
ax1.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))
ax2 = ax1.twinx()
ax2.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))

ax2.plot(t,I,c=colors[1])
ax1.plot(t,u,c=colors[0])

ax1.tick_params('y', colors=colors[0])
ax2.tick_params('y', colors=colors[1])

#plt.tight_layout()
ax1.set_xlabel("t")
ax1.set_ylabel("u",color=colors[0])
ax2.set_ylabel("I",color=colors[1])

ax1.set_xlim([20.,1000.])

#import pdb
#pdb.set_trace()

plt.savefig("rate_dyn_u_illustr.svg")

plt.show()