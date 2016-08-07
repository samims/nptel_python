def gcd(m,n):
	if (n>m):
		(m,n) = (n,m)
	while(m%n) != 0:
		(m,n) = (n, m%n)
	return n