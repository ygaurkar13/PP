dec_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
'''
def str_to_int_using_recursion_l_to_r(text):
	text_len=len(text) 
	if text_len==0:
		return 0
	elif text_len==1:
		return dec_dict[text]
	else:
		return dec_dict[text[0]]*10**(text_len-1)+ str_to_int_using_recursion(text[1:])	#instead of ** --> pow(10,text_len-1) 
text='12'
print(str_to_int_using_recursion(text))	
'''
#below is having errors:
def str_to_int_using_recursion_r_to_l(text):
	order=-1
	text_len=len(text) 
	if text_len==0:
		return 0
	elif text_len==1:
		return dec_dict[text]
	else:
		order+=1
		return dec_dict[text[-1]]*10**order + str_to_int_using_recursion_r_to_l(text[text_len:-1]) #pow(10,order)
text='1213'
print(str_to_int_using_recursion_r_to_l(text))
