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


def change_case1(string,style):
	if style in ("Z","z"):
		y=[]
		for i,ele in enumerate(string):
			if "A"<=ele<="Z":
				if i%2==0:
					y.append(ele if "A"<=string[0]<="Z" else chr(ord(ele)+32))
				else:
					y.append(chr(ord(ele)+32) if "A"<=string[0]<="Z" else ele)
			elif "a"<=string[0]<="z":
				if i%2==0:
					y.append(ele if "a"<=string[0]<="z" else chr(ord(ele)-32))
				else:
					y.append(chr(ord(ele)-32) if "a"<=string[0]<="z" else ele)
	else:
		y.append(ele)
	return "".join(y)
s="AbCdefg"
print(change_case1(s,"Z"))
print(change_case1(s,"z"))



def change_case1(string,style):
	if style =="zigzag2":
		y=[]
		for i,ele in enumerate(string):
			if "A"<=ele<="Z":
				if i%2==0:
					y.append(chr(ord(ele)+32))
				else:
					y.append(ele)
			elif "a"<=string[0]<="z":
				if i%2==0:
					y.append(ele)
				else:
					y.append(chr(ord(ele)-32))
			else:
				y.append(ele)
	else:
		return "Invalid Syntax"
	return "".join(y)
s="abcdef"
print(change_case1(s,"zigzag2"))





