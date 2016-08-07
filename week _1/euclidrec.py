def gcd(m,n):
	if (n>m):
		(m,n) = (n,m)
	if (m%n) == 0:
		return(n)
	
	return(gcd(n,m%n))

print(gcd(21,15))