def get_palindrome_count(L1):
	Count,reg_no =0,9
	for element in L1:
		if isinstance(element,(list, tuple,set)):
			Count+=(get_palindrome_count(list(element)))
		elif (isinstance(element , str) and len(element)%reg_no==5 ) :
			Count+=(element==element[::-1])
		else:
			return "Raise Value Error"
	return Count
L1=['11111','12221',['11111','11111222211111','13231133113231']]
print(get_palindrome_count(L1))
