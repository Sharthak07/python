x= input("enter four numbers: ").split(',')
if x[0] >= x[1]and x[0] >= x[2]and x[0] >= x[3]:
    print(f"{x[0]} is the greatest number")
elif x[1] >= x[0]and x[1] >= x[2]and x[1] >= x[3]:
    print(f"{x[1]} is the greatest number")
elif x[2] >= x[0]and x[2] >= x[1]and x[2] >= x[3]:
    print(f"{x[2]} is the greatest number")
else:
    print(f"{x[3]} is the greatest number")



marks1= int(input("enter marks1: "))
marks2= int(input("enter marks2: "))
marks3= int(input("enter marks3: "))

total_percentage= (marks1+marks2+marks3)/300 * (100) 
if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are passed", total_percentage)
else:
    print("You are failed", total_percentage)


#spam detector
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")



username= input("Enter your username: ")
if(len(username) < 10):
    print("username is less than 10 characters")
else:
    print("username is greater than 10 characters")


l1= ["subham","sarthak","rohit","vijay"]  # all lowercase
name= input("Enter your name: ").lower()   # converts input to lowercase first
if(name in l1):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")