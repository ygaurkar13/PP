def get_even_odd_count(L1):
	even_num_count,odd_num_count=0,0
	for i in L1:
		if i%2==0:
			even_num_count+=1
		else:
			odd_num_count+=1
	return even_num_count,odd_num_count
	
def get_even_odd_count_by_boolean_value(L1):
	even_num_count,odd_num_count=0,0
	for i in L1:
		if i%2:
			odd_num_count+=1
		else:
			even_num_count+=1
	return even_num_count,odd_num_count
	


L1=list(range(-1000,1001,1))
print(get_even_odd_count(L1))


