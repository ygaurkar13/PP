'''for loop and if else
def fun1(n):
	mid=len(n)//2
	result=""
	for i in range(len(n)):
		if i>=mid:
			result +=n[i].upper()
		else:
			result +=n[i]
	return result
n="samsamsam"
print(fun1(n))
'''
''' join()  
def fun1(n):
	mid=len(n)//2
	result="".join([n[i].upper() if i>=mid else n[i] for i in range(len(n))])
	return result
n="satyammishra"
print(fun1(n))
'''
'''Slicing and concatenation
def fun1(n):
	mid=len(n)//2
	result=n[mid:].upper()
	return n[:mid]+result
n="satyammishra"
print(fun1(n))
'''
'''Slicing for loop and index'''
def fun1(n):
	mid=len(n)//2
	for i in range(len(n)):
		
		 
