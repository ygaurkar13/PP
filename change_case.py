def change_case(string,style):
	if style in ("C","c"):
		y=[]
		for ele in s:
			if "a"<=ele<="z":
					y.append(chr(ord(ele)-32))
			else:
				y.append(ele)
	return y
a="sggsieandt"
print(change_case(a,"c"))
print(change_case(a,"C"))

def change_case(string,style):
	if style in ("S","s"):
		y=[]
		for ele in string:
			if "A"<=ele<="Z":
					y.append(chr(ord(ele)+32))
			else:
				y.append(ele)
	return y
a="SGGSIEANDT"
print(change_case(a,"s"))
print(change_case(a,"S"))



def change_case(string,style):
	if style in ("R","r"):
		y=[]
		for ele in string:
			if "A"<=ele<="Z":
				y.append(chr(ord(ele)+32))
			elif "a"<=ele<="z":
				y.append(chr(ord(ele)-32))
			else:
				y.append(ele)
	return y
a="SgGsIeAnDt"
print(change_case(a,"r"))
print(change_case(a,"R"))








