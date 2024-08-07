def print_p(length):
    column = (length * 2) + 3
    kite = (length * 2) + 1
    lst_row = length

    # Upper part of the kite
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 2):
            if j == (kite // 2) - i + 1:
                print("+", end="")
            elif j == (kite // 2) + i + 1:
                print("+", end="")
            else:
                print(" ", end="")
        print("")
        
       # Middle part with the number
    for i in range(1):
        for j in range(0, kite + 2):
            if j == i + 1:
                print("+", end="")
            elif j == ((kite + 2) // 2):
                print(" ", end="")
            elif j == kite:
                print("+", end="")
                break
            else:
                print(" ", end="")
        print("")
        
        # Lower part of the kite
    for i in range(0, (kite // 2) - 1):
        for j in range(0, kite + 1):
            if j == i + 2:
                print("-", end="")
            elif j == (kite + 1) - i - 2:
                print("-", end="")
            else:
                print(" ", end="")
        print("")
        
     
    for i in range(0, column//2):
            print(" ", end="")
    print("-")
    return ""

print_p(2)        
        
