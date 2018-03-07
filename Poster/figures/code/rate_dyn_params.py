#!/usr/bin/env python3

import numpy as np

N=3

t_end=100

s=10*2**0.5
a=.5
g_0=100.
a_g=4./g_0
shift=g_0/2.
T_x=2.
T_y=2.

E_exc_syn = 10.
E_inh_syn = -10.
tau_g = 20.

r_start = np.zeros((N,2))

W_combined = np.array([	[0.,0.,0.],
						[0.,0.,-.1],
						[0.,.1,0.]])

#sim_prot = [[0,100,200],["I_ext = -10.","I_ext = 10.","I_ext = -10."]]
sim_prot = [[0],["I_ext[:1] = .0"]]