def regla30(a,i,s):
	if a and i and s ==0:
		x=0
	else:
		if a and i ==1 and s==0:
			x=0
		if a and s ==1 and i ==0:
			x=0
		if s and i ==0 and a==1:
			x=1
		if s and i ==1 and a ==0:
			x=1
		if i ==1 and a and s ==0:
			x=1
		if s ==1 and a and i ==0:
			x=1
		if a and i and s ==0:
			x=0
		return(x)
