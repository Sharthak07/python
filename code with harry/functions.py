def greatest():                                   #greatest number using function call
    x= int(input("enter three numbers: "))
    y= int(input("enter three numbers: "))
    z= int(input("enter three numbers: "))

    if (x>y and x>z):
        print(x, "is greater number")
    elif(y>x and y>z):
        print(y,"is greater number" )
    elif(z>y and z>x):
        print(z,"is greater number" )
    else:
        print("invalid character/number")

greatest()


def temp_convert(n):   # fahrenheit to celsius conversion
    n=(n*1.8)+32
    return n

a=temp_convert(25)
print(a)


def inch_cm(n):  # inch to cm conversion
    n=n*2.54
    return n

a=inch_cm(14)
print(a)


#resursion function
def sum(n):
    if (n==1):    #base condition, if not present it will go into infinite loop and give error
        return 1
    return sum(n-1)+n    # Keep going down to sum(1), then come back up adding each n

print(sum(3))

 