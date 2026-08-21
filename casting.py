
#typecasting & print
a= float(input("Enter a number: "))
b= float(input("Enter another number: "))
c= float(input("Enter another number: "))
sum =(a+b+c)
print("sum:", sum)
print("average:", round(sum/3, 2))


# #find and presence
name= input("Enter your name: ")
print(name.startswith('S')) or print(name.startswith('s'))


# if else basic 
name = input("Enter your name: ")
if name.startswith('S'):
    print(True)
elif name.startswith('s'):
    print(True)
else:
    print(False)