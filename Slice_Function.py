def Slice_Function(obj,start=None,stop=None,step=None):
	if step is None:
		step=1
		
	if start is None:
		start=0 if step>0 else len(obj)-1
	if stop is None:
		stop=len(obj) if step>0 else -1
	
	
	if start<0:
		start += len(obj)
	if stop<0:
		stop += len(obj)
		
	result=[]
	
	i=start
	if step>0:
		while i<stop :
			result.append(obj[i])
			i+=step
	else:
		while i>stop:
			result.append(obj[i])
			i+=step
	return result
	

obj=[1,2,3,4,5,6,7]
obj1=['a','b','c','d','e']
print(Slice_Function(obj,0,len(obj),1))
print()
print(Slice_Function(obj1,0,len(obj1),1))
print()
print(Slice_Function(obj,-1,-len(obj)-1,-1))
print()
print(Slice_Function(obj1,-1,-len(obj1),-1))
print()
print(Slice_Function(obj1,start=-1))

		
	
