#!/usr/bin/env python3

import numpy as np

N=1

t_end=200

r_start = np.array(([[1.,1.]]))

s=10*2**0.5
a=.2
g_0=60.
a_g=.1/2.**.5
shift=30.
T_x=.1
T_y=8.

E_exc_syn = 10.
E_inh_syn = -10.
tau_g = 20.

W_combined = np.array([[0.]])*2.

sim_prot = [[0,133,166,t_end-1.],["I_ext = -10.","I_ext = 10.","I_ext = -10.","np.save('../data/r_rec_rate_dynamics_step.npy',r_rec[int((t_end-100.)/dt):int((t_end-1.)/dt),0,:])"]]
