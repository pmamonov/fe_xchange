from numpy import exp

def Ea(v1,v2,T):
	kb=2e-3
	p1=exp(-v1/kb/T)
	p2=exp(-v2/kb/T)
	return kb*T**2/((p2*p1).sum()/p1.sum()/p2.sum()) * ( ((v2+v1)/kb/T**2*p2*p1).sum() * p2.sum() * p1.sum() - (p1*p2).sum()* (p2.sum()*(p1*v1/kb/T**2).sum()+p1.sum()*(p2*v2/kb/T**2).sum()))/(p2.sum()*p1.sum())**2
