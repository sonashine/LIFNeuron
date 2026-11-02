import numpy as np
import matplotlib.pyplot as plt

tau_m = 10.0  # Membrane time constant (ms)
V_rest = -65.0  # Resting potential (mV)
V_reset = -65.0  # Reset potential (mV)
V_th = -50.0  # Threshold potential (mV)
R = 10.0  # Membrane resistance (MΩ)
t_ref = 2.0  # Refractory period (ms)

dt, T = 0.1, 200.0 
t=np.arange(0,T,dt)
I=np.zeros_like(t)
I[(t>=50) & (t<150)]=2.0
V= np.full_like(t,V_rest)
spikes=[]
last_spike = -np.inf

for i in range(1,len(t)):
    if t[i] - last_spike < t_ref:
        V[i]=V_reset
        continue
    dV=(-(V[i-1]-V_rest)+R*I[i-1])/tau_m
    V[i]=V[i-1]+dt*dV
    if V[i]>=V_th:
        V[i-1]=0
        V[i]=V_reset
        spikes.append(t[i])
        last_spike = t[i]

fig, (ax1,ax2) = plt.subplots(2,1, figsize=(9,5) , sharex=True, gridspec_kw={"height_ratios":[3,1]})
ax1.plot(t,V,color="k",lw=1)
ax1.axhline(V_th,color="r", ls="--", lw=0.8,label="Threshold")
ax1.set_ylabel("Membrane Potential (mV)")
ax1.legend(loc="upper right")

ax2.plot(t,I,color="tab:blue")
ax2.set_ylabel("Input (nA)")
ax2.set_xlabel("Time (ms)")
plt.tight_layout()
plt.show()

print("Spike times (ms):", spikes)