dec_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str_to_int_using_enumerate_l_to_r(text):
	text_len=len(text)	#len of text
	if text_len==0: 	#border case for 0 and 1 
		return 0
	elif text_len==1:
		return dec_dict[text]
	else:				#for length greater than 1 
		text_len-=1   		#align length of text for power  
		res=0				#initialize result 
		for i, ch in enumerate(text):#loop to iter through text using enumerate to use indx and char as well
			res=res+dec_dict[ch]*10**text_len	 
			text_len-=1
		return res	
text='123'
print(str_to_int_using_enumerate_l_to_r(text))

def str_to_int_using_enumerate_r_to_l(text):
	order=-1			#order initialized to -1 
	text_len=len(text) 
	if text_len==0:   		#for  border case of 0 
		return 0		
	elif text_len==1:		#for border case of 1
		return dec_dict[text]
	else:
		order+=1		#updated to make it 0 for last index point char
		res=0				#result initialized
		for i, ch in enumerate(text[::-1]):   #reversed string is passed to access from last index char
			res=res+dec_dict[ch]*10**order		#res calculated from last index char
			order+=1				#order updated reversed way
		return res					
text='123'
print(str_to_int_using_enumerate_r_to_l(text))
				
