#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 20/1.25})

u = np.load("spike_dyn_u.npy")
t = np.load("t_axis.npy")

fig_size = (10.,10.)
axis_size = (6.456,4.670)
axis_pos = ((fig_size[0]-axis_size[0])/2.,(fig_size[1]-axis_size[1])/2.)

fig,ax = plt.subplots(1,1,figsize=fig_size)
ax.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))
plt.plot(t,u)
#plt.tight_layout()
plt.xlabel("t")
plt.ylabel("u")

plt.savefig("spike_dyn_u_illustr.svg")

plt.show()