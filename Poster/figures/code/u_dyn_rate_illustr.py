#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 20/1.25})

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

r_rec = np.load("../data/r_rec_rate_dynamics_step.npy")
u_rec = (r_rec[:,0] + r_rec[:,1])/2.**.5

n_t = u_rec.shape[0]
dt = 100./n_t
t_range = np.array(range(n_t))*dt

I = np.ones((n_t))*-10.
I[int(33./dt):int(66./dt)] = 10.

fig_size = (20.,10.)
axis_size = (13.9,4.)
axis_pos = ((fig_size[0]-axis_size[0])/2.,(fig_size[1]-axis_size[1])/2.)

fig,ax = plt.subplots(1,1,figsize=fig_size)
axI = ax.twinx()
ax.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))
axI.set_position((axis_pos[0]/fig_size[0],axis_pos[1]/fig_size[1],axis_size[0]/fig_size[0],axis_size[1]/fig_size[1]))

ax.plot(t_range,u_rec,c=colors[0])
axI.plot(t_range,I,c=colors[1])

ax.set_xlim([0.,100.])
axI.set_xlim([0.,100.])
axI.set_ylim([-12.,50.])

ax.set_xlabel("t")
ax.set_ylabel("u",color=colors[0])
axI.set_ylabel("I",color=colors[1])

ax.tick_params('y', colors=colors[0])
axI.tick_params('y', colors=colors[1])


plt.savefig("../graphics/rate_dyn_u_step_illustr.svg")

plt.show()

