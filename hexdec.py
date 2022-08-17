# Python program to convert hexadecimal to decimal

def HexDecimal(n):  #user-defined function
    return int(n, 16)
    
# take inputs
num = input('Enter hexadecimal number: ')

# calling function and display result
print('The decimal value is =', HexDecimal(num))
