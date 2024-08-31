def S0(text):
	if text[0]=="b":
		if len(text)==1:
			return "rejected"
		else:
			return S0(text[1:])
	elif text[0]=="a":
		if len(text)==1:
			return "accepted"
		else:
			return S1(text[1:])
	else:
		return "rejected"
		
def S1(text):
	if text[0]=="a":
		if len(text)==1:
			return "accepted"
		else:
			return S0(text[1:])
	elif text[0]=="b":
		if len(text)==1:
			return "rejected"
		else:
			return S1(text[1:])
	else:
		return "accepted"	
	
text="abbbb"
print(S0(text))	
