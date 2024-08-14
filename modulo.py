def modulo(numerator,denominator):
 k=numerator//denominator
 m=k*denominator
 z=numerator-m
 return z
 
print(modulo(4,3)) 
 
 
def modulo(n , d):
	q = int(n/d);
	ans = (n-(q*d))
	return ans

n = int(input("Enter n : "))
m = int(input("Enter m : "))
print(modulo(n,m))
