def find_sl(newList) :
	if len(newList) == 0 or len(newList) == 1:
		return -1;
	second = -1000000000000;
	maxVal = newList[0];
	for val in newList :
		if val > maxVal :
			if second < maxVal :
				second = maxVal;
			maxVal = val;
		elif val < maxVal and val > second :
			second = val;
	return second;
def find_ss(newList) :
	if len(newList) == 0 or len(newList) == 1:
		return -1;
	
	minVal = newList[0]
	second = 10000000000000;
	for val in newList :
		if val < minVal :
			if second > minVal :
				second = minVal;
			minVal = val;
		elif val > minVal and val < second :
			second = val;
	return second;
newList =[];
def get_SL_SS(input_data) :
	for data in input_data :
		if isinstance(data,int) :
			newList.append(data);
		elif isinstance(data,str) :
			continue;
		elif isinstance(data,(float,complex)) :
			continue;
		elif isinstance(data,(tuple,set)) :
			get_SL_SS(list(data));
		elif isinstance(data,(dict)) :
			get_SL_SS(list(data.values()));
			get_SL_SS(list(data.keys()));
		elif isinstance(data,list) :
			for val in data :
				if isinstance(val,int) :
					newList.append(val);
	
get_SL_SS({2})
print(find_sl(newList));
print(find_ss(newList));
def find_sl(newList) :
	if len(newList) == 0 or len(newList) == 1:
		return -1;
	second = -1000000000000;
	maxVal = newList[0];
	for val in newList :
		if val > maxVal :
			if second < maxVal :
				second = maxVal;
			maxVal = val;
		elif val < maxVal and val > second :
			second = val;
	return second;
def find_ss(newList) :
	if len(newList) == 0 or len(newList) == 1:
		return -1;
	
	minVal = newList[0]
	second = 10000000000000;
	for val in newList :
		if val < minVal :
			if second > minVal :
				second = minVal;
			minVal = val;
		elif val > minVal and val < second :
			second = val;
	return second;
newList =[];
def get_SL_SS(input_data) :
	for data in input_data :
		if isinstance(data,int) :
			newList.append(data);
		elif isinstance(data,str) :
			continue;
		elif isinstance(data,(float,complex)) :
			continue;
		elif isinstance(data,(tuple,set)) :
			get_SL_SS(list(data));
		elif isinstance(data,(dict)) :
			get_SL_SS(list(data.values()));
			get_SL_SS(list(data.keys()));
		elif isinstance(data,list) :
			for val in data :
				if isinstance(val,int) :
					newList.append(val);
	
get_SL_SS({2})
print(find_sl(newList));
print(find_ss(newList));
