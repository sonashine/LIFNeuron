# LIFNeuron

A minimal Python implementation of the Leaky Integrate-and-Fire neuron model

The Model

The membrane potential V evolves according to:

τ_m · dV/dt = −(V − V_rest) + R · I(t)
When V reaches the threshold V_th, the neuron emits a spike and V is reset to V_reset.
After each spike, the neuron stays silent for a refractory period t_ref.
The minimum current needed to make the neuron fire (the rheobase) is I = (V_th − V_rest) / R, which is 1.5 nA with the default parameters.

Default Parameters
Parameter	Symbol	Value	Unit
Membrane time constant	tau_m	10.0	ms
Resting potential	V_rest	−65.0	mV
Reset potential	V_reset	−70.0	mV
Spike threshold	V_th	−50.0	mV
Membrane resistance	R	10.0	MΩ
Refractory period	t_ref	2.0	ms
Time step	dt	0.1	ms
Simulation length	T	200.0	ms
Step current amplitude	I	2.0 (50–150 ms)	nA