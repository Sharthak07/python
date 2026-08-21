a= float(input("enter the value of a:"))
b= float(input("enter the value of b:"))
operation= (input("enter the operation: (+, -, *, /, %, **):"))

if operation == '+':
    print("sum:", a+b)
elif operation == '-':
    print("subtraction:", a-b)
elif operation == '*':              
    print("multiplication:", a*b)
elif operation == '/':
    print("division:", a/b)
elif operation == '%':
    print("modulus:", a%b)
elif operation == '**':
    print("exponent:", a**b)
else:
    print("invalid operation")