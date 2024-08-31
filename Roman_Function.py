def rom(text,text_base):
    def to_integer(text,text_base):
        try:
            return int(text,text_base)
        except ValueError:
            raise ValueError("Invalid number or base")

    def integer_to_roman(num):
        roman_numerals = [
            (100000, 'C̅'),
            (90000, 'XC̅'),
            (50000, 'L̅'),
            (40000, 'XL̅'),
            (10000, 'X̅'),
            (9000, 'MX̅'),
            (5000, 'V̅'),
            (4000, 'MV̅'),
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        if num <= 0:
            raise ValueError("Number must be greater than 0")
        if num >= 100000:
            raise ValueError("Number out of range (1 - 99999)")

        result = ""
        for value, numeral in roman_numerals:
            while num >= value:
                result += numeral
                num -= value
        return result

    integer_value = to_integer(text, text_base)
    
    roman_value = integer_to_roman(integer_value)
    
    return roman_value

print(rom("1111", 2))  
print(rom("1A3", 16))  
print(rom("255", 10))
print(rom("123",4)) 
print(rom("1234",5))
		

