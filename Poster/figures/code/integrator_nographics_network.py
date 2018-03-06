#!/usr/bin/env python3



import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.size"] = 8.
import pdb

#from supercrit_hopf_params import *
from subcrit_hopf_params_forward import *
#from subcrit_hopf_params_backward import *

#from bistable_saddle_params import *
#from inv_circle_saddle_params import *

#from rate_dyn_params import *
#from spiking_dyn_params import *

def length(r):
	return (r[0]**2+r[1]**2)**0.5

def step(r,I):
	ra=r+0.5*dt*f(r,I,T_x,T_y)
	rb=r+0.5*dt*f(ra,I,T_x,T_y)
	rc=r+dt*f(rb,I,T_x,T_y)
	return r+(dt/6)*(f(r,I,T_x,T_y)+2*(f(ra,I,T_x,T_y)+f(rb,I,T_x,T_y))+f(rc,I,T_x,T_y))

def F(x,s,a):
	return -x + s/(1+np.exp(-(a*(x-s/4))))
def G(x,g_0,a_g,I):
	return g_0/(1+np.exp(-(a_g*(x-I))))-shift


def f(psi,I,T_x,T_y):
	return np.array([(F(psi[0],s,a)-psi[1])/T_x,(G(psi[0],g_0,a_g,I)-psi[1])/T_y])

def nullcly(v,I):
	return G(v,g_0,a_g,I)

def nullclx(v,I):
	return F(v,s,a)


dim=12.7

zoom=400

dt=0.01


t=0
n_t = int(t_end/dt)



r_rec = np.ndarray((n_t,N,2))
u_rec = np.ndarray((n_t,N))

u=np.zeros(N)*0.

I=np.zeros(N)*0.

r=r_start[:]#np.zeros((N,2))

g_exc = np.zeros((N))
g_inh = np.zeros((N))

g_exc_rec = np.ndarray((n_t,N))
g_inh_rec = np.ndarray((n_t,N))

trigger=np.ones(N)


exc_ind = np.where(W_combined>0)
inh_ind = np.where(W_combined<0)

W_exc = np.zeros((N,N))
W_inh = np.zeros((N,N))

W_exc[exc_ind[0],exc_ind[1]] = W_combined[exc_ind[0],exc_ind[1]]

W_inh[inh_ind[0],inh_ind[1]] = -W_combined[inh_ind[0],inh_ind[1]]


I_ext_rec = np.ndarray((n_t,N))
I_rec = np.ndarray((n_t,N))

I_exc_syn_rec = np.ndarray((n_t,N))
I_inh_syn_rec = np.ndarray((n_t,N))

I_ext = np.zeros((N))#np.linspace(-20.,30.,n_t)



for t in tqdm(range(n_t)):
	
	if int(t*dt) in sim_prot[0]:
		exec(sim_prot[1][sim_prot[0].index(int(t*dt))])


	I_exc_syn=np.dot(W_exc,u)
	I_inh_syn=np.dot(W_inh,u)
	
	#I_ext += dt*(mean_u - u.mean())*0.1
	I_exc_syn_rec[t,:] = I_exc_syn
	I_inh_syn_rec[t,:] = I_inh_syn

	g_exc += dt*(-g_exc + I_exc_syn)/tau_g
	g_inh += dt*(-g_inh + I_inh_syn)/tau_g

	g_exc_rec[t,:] = g_exc
	g_inh_rec[t,:] = g_inh

	I = g_exc*(E_exc_syn - u) + g_inh*(E_inh_syn - u) + I_ext

	I_ext_rec[t,:] = I_ext	
	I_rec[t,:] = I

	for k in range(N):
		
	
		
		
	
	
		r[k,:]=step(r[k,:],I[k])
	
		u[k]=(r[k,0]+r[k,1])/(2**0.5)
	
		
	
		if f(r[k,:],I[k],T_x,T_y)[1]<=0 and trigger[k]==0:
			trigger[k]=1
			
			
		if f(r[k,:],I[k],T_x,T_y)[1]>0 and trigger[k]==1:
			trigger[k]=0
			
		#data.write(str(u[k])+" "d)
	
	r_rec[t,:,:] = r
	u_rec[t,:] = u
	
	#data.write("\n")
	#if t>=t_end:
	#	sys.exit(0)
	#	data.close()
fig,ax = plt.subplots(N,2,figsize=(15,10))
labels=["isolated reference neuron","exc. neuron","inh. neuron"]
if N > 1:
	for k in range(N):
		ax[k,0].plot(np.array(range(n_t))*dt,u_rec[:,k],c="k")
		ax[k,0].set_title(labels[k])
		ax[k,0].set_xlabel("t")
		ax[k,0].set_ylabel("u")

		ax[k,1].plot(r_rec[:,k,0],r_rec[:,k,1],c="k")
		ax[k,1].grid()
		ax[k,1].set_xlabel("x")
		ax[k,1].set_ylabel("y")
		ax[k,1].set_title(labels[k])
else:
	ax[0].plot(np.array(range(n_t))*dt,u_rec[:,k],c="k")
	ax[0].set_title(labels[k])
	ax[0].set_xlabel("t")
	ax[0].set_ylabel("u")

	ax[1].plot(r_rec[:,k,0],r_rec[:,k,1],c="k")
	ax[1].grid()
	ax[1].set_xlabel("x")
	ax[1].set_ylabel("y")
	ax[1].set_title(labels[k])

plt.tight_layout()	

plt.show()
pdb.set_trace()

