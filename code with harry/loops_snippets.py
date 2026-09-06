number= int(input("enter a number: "))   #multiplication table of a number using while loop
i=1
while (i<=10):
    print(number*i)
    i+=1


n= int(input("Enter a number: "))  
for i in range(n, 0, -1):
    print("*" * i)  # prints a triangle pattern using for loop


l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello " + name)
    

# sum of natural no
num= int(input("enter a number: "))  
i=1
total=0
while (i<=num):     # indenttion is imp, print(total) if inside the loop will print the total after every iteration, if outside the loop only prints the final total.
    total=total+i
    i=i+1
print(total)


n = int(input("Enter n: "))  # very important pattern printing using for loop, pyramid pattern
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    
    print(" " * spaces + "*" * stars)



n = int(input("Enter the number: "))  # box printing using for loop, hollow rectangle pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")

    print("")


