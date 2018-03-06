#!/usr/bin/env python3

import numpy as np

N=1

t_end=100

r_start = np.array(([[2.,2.]]))

s=10*2**0.5
a=.8
g_0=60.
a_g=6.
shift=-.7
T_x=1.
T_y=.7

E_exc_syn = 10.
E_inh_syn = -10.
tau_g = 20.

W_combined = np.array([[0.]])*2.

sim_prot = [[0,t_end-1.],["I_ext = 3.475","np.save('../data/r_rec_bistable_saddle.npy',r_rec[int((t_end-10.)/dt):int((t_end-1.)/dt),0,:])"]]