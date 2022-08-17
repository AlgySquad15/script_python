# Python program to convert decimal to binary using recursion

def DecimalBinary(n):   #user-defined function
    if n >= 1:
        DecimalBinary(n // 2)
    print(n % 2, end = '')
 
# take input
num = int(input('Enter any decimal number: '))

# calling function and display result
print('Binary value: ')
DecimalBinary(num)