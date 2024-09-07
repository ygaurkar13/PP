def binary_subtraction(a, b):
    
  
    bits = max(a.bit_length(), b.bit_length()) + 1
    
   
    b_twos_complement = ((1 << bits) - 1) - b + 1

    
    result = a + b_twos_complement
    
   
    result = result & ((1 << bits) - 1)

    if result >= (1 << (bits - 1)):
        result -= (1 << bits)
    result_bin = format(result & ((1 << bits) - 1), f'0{bits}b')
    
    return result, result_bin


a = 12
b = 5
result, result_bin = binary_subtraction(a, b)
print(f"Decimal result: {result}")
print(f"Binary result (two's complement): {result_bin}")
