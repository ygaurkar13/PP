def check_performance_in_percent(approaches):
	total_time_taken_by_approaches=[]
	for approach in approaches:
		start_time=time.time()
		approach()
		end_time=time.time()
		total_time_taken_by_approaches.append(end_time-start_time)
	time_taken_by_base_approach=total_time_taken_by_approaches[0]
	percent_faster=[]
	for i, time_app in enumerate(total_time_taken_by_approaches[1:]):
		 percent_faster.append(((time_taken_by_base_approach-total_time_taken_by_approaches[i])/time_taken_by_base_approach)*100)
	for ele in percent_faster:
		print("approach is %0.1f"%(ele))
		
	
	
