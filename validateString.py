inputs = {'{', '(', '<', '[', '}', ')', '>', ']'}

def validateString(text):
    curly, rnd, ang, sqr = 0, 0, 0, 0
    for char in text:
        if char not in inputs:
            return False  # Return False for invalid characters
        elif char == '{':
            curly += 1
        elif char == '}':
            if curly == 0:
                return False
            curly -= 1
        elif char == '(':
            rnd += 1
        elif char == ')':
            if rnd == 0:
                return False
            rnd -= 1
        elif char == '<':
            ang += 1
        elif char == '>':
            if ang == 0:
                return False
            ang -= 1
        elif char == '[':
            sqr += 1
        elif char == ']':
            if sqr == 0:
                return False
            sqr -= 1

    return curly == 0 and rnd == 0 and ang == 0 and sqr == 0 

def count_valid_invalid_String(strings):
    valid_count = 0
    invalid_count = 0
    for text in strings:
        if validateString(text):
            valid_count += 1
        else:
            invalid_count += 1
    return (valid_count, invalid_count)

strings_list = ["<<<d>>>", "{[()(a)]}", "{[(])2}", "((()))", "{<[bg]>}"]
result = count_valid_invalid_String(strings_list)
print(result) 
