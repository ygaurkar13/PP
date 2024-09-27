def fcfs(burst_time,arrival_time,number_of_processes):
	waiting_time=[0]*5
	waiting_time[0]=0
	for i in range(1,number_of_processes,1):
		waiting_time[i]=(arrival_time[i-1]+burst_time[i-1]+waiting_time[i-1])-arrival_time[i]
		print("After Process",i,":",waiting_time)
	total_waiting_time=0
	average_waiting_time=0
	for i in range(len(waiting_time)):
		total_waiting_time+=waiting_time[i]
	average_waiting_time=total_waiting_time/number_of_processes
	print("Total Waiting Time:",total_waiting_time)
	print()
	print("Average Waiting Time",average_waiting_time)
burst_time=[4,3,1,2,5]
arrival_time=[0,1,2,3,4]	
number_of_processes=5
print(fcfs(burst_time,arrival_time,number_of_processes))	
	

