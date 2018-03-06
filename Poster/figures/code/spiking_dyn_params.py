#!/usr/bin/env python3

import numpy as np

N=3

t_end=300

s=10*2**0.5
a=1.85
g_0=400.
a_g=2.
shift=4.0
T_x=.25
T_y=25.



E_exc_syn = 10.
E_inh_syn = -10.
tau_g = 20.

W_combined = np.array([	[0.,0.,0.],
						[0.,0.,-1.],
						[0.,1.,0.]])*2.

sim_prot = [[],[]]