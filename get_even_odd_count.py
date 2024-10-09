import time
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

def get_even_odd_count_binary(L1):
	even_num_count,odd_num_count=0,0
	for num in L1:
		if bin(num)[-1]==0:
			even_num_count+=1
		else:
			odd_num_count+=1
		
def get_even_odd_count_app4(L1):
	even_num_count,odd_num_count=0,0
	for i in L1:
		t=i%2
		odd_num_count+=t
		even_num_count=1-t


def check_performance_in_percent(approaches):
	total_time_taken_by_approaches=[]
	for approach in approaches:
		start_time=time.time()
		approach(L1)
		end_time=time.time()
		total_time_taken_by_approaches.append(end_time-start_time)
	time_taken_by_base_approach=total_time_taken_by_approaches[0]
	percent_faster=[]
	for i, time_app in enumerate(total_time_taken_by_approaches[1:]):
		 percent_faster.append(((time_taken_by_base_approach-total_time_taken_by_approaches[i])/time_taken_by_base_approach)*100)
	for ele in percent_faster:
		print("approach is %0.1f"%(ele),"percent faster than base approach")
		
	
	
					

L1=list(range(-1000,1001,1))
print(check_performance_in_percent([get_even_odd_count_app4,get_even_odd_count,get_even_odd_count_by_boolean_value,get_even_odd_count_binary]))


