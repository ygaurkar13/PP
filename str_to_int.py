dec_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str_to_int(text):
	if len(text)==0:   
		return 0
	elif len(text)==1:
		return dec_dict[text]
	else:
		length_of_text=len(text)
		num,n=0,length_of_text-1
		for ele in text:
			if ele not in dec_dict:
				return "ValueError"
			else:	
				num=num*10 + dec_dict[ele]
		return num
def decimal_subtraction(text1, text2):
	num1 = str_to_int(text1)
	num2 = str_to_int(text2)

	def get_digits(num):
		digits = []
		while num > 0:
			digits.append(num % 10)
			num //= 10
		return digits or [0]  # Handle the case for zero

    # Extract digits
	num1_digits = get_digits(num1)
	num2_digits = get_digits(num2)
 
	max_len = max(len(num1_digits), len(num2_digits))
	num1_digits.extend([0] * (max_len - len(num1_digits)))
	num2_digits.extend([0] * (max_len - len(num2_digits)))
    
    
	result_digits_list = []
	borrow = 0
    
	for digit1, digit2 in zip(num1_digits, num2_digits):
		subtr_of_num = digit1 - digit2 - borrow
		if subtr_of_num < 0:
			subtr_of_num += 10
			borrow = 1
		else:
			borrow = 0
		result_digits_list.append(subtr_of_num)
    
	while result_digits_list and result_digits_list[-1] == 0:
		result_digits_list.pop()

	if result_digits_list:
		result_string = ''.join(map(str, result_digits_list[::-1]))
	else:
		result_string = '0'
    
	return result_string

OP = decimal_subtraction("126", "125")
print(OP)	
	
	
	
	
	
	

				
			
