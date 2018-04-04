import numpy as np

def T_anneal(T, ii, num_steps, num_burnin):

    #implement annealing code here
	T_start = 10

	if (num_burnin > 0) and (ii < num_burnin):
		alpha = np.exp( np.log(T/T_start) / num_burnin )
		T_a = T_start * alpha ** (ii)
	else:
		T_a = T

	#print(T_a)
	return float(T_a)

def B_anneal(B, ii, num_steps, num_burnin):

    #implement annealing code here
    
	B_start = 10
	if (num_burnin > 0) and (ii < num_burnin):
		alpha = np.exp( np.log((B+0.01)/B_start) / num_burnin )
		B_a = B_start * alpha ** (ii)
	else:
		B_a = B

	return float(B_a)