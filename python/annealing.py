def T_anneal(T, ii, num_steps, num_burnin):

    #implement annealing code here
	
	T_start = 10
	alpha = e ** ( log(T/T_start) / num_burnin )
	
	if ii < num_burnin:
		T_a = T_start * alpha ** (ii)
	else:
		T_a = T

	return float(T_a)

def B_anneal(B, ii, num_steps, num_burnin):

    #implement annealing code here
    
	B_start = 10
	alpha = e ** ( log(B/B_start) / num_burnin )
	
	if ii < num_burnin:
		B_a = B_start * alpha ** (ii)
	else:
		B_a = B
	return float(B_a)