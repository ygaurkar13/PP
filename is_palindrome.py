def is_palindrome(s):
	return s==s[::-1]
def is_symmetrical(s):
	length =len(s)
	mid=length//2
	if length %2 ==0:
		return s[:mid]==s[mid:]
	else:
		return s[:mid]==s[mid+1:]
	string ='lawnlawn'
	if is_palindrome(string):
		print("is palindrome")
	else:
		print("not palindrome")
	    
	if is_symmetrical(string):
		print("is symmetrical")
	else:
		print("not symmetrical")
s="212"
print(is_palindrome(s))
print(is_symmetrical(s))
