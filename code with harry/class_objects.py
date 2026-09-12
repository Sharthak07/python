# class programmer:                   #simple class and object creation
#     name= "rohan"
#     language= "python"
#     salary= 50000
#     company= "Microsoft"

# data= programmer()
# print(data.name,data.salary)



# class calculator:
#     pass
#     def square(self):
#         a= int(input("enter a no: "))
#         a=a**2
#         print(f"square is: {a}")

#     def cube(self):
#         b= int(input("enter a no: "))
#         b=b**3
#         print(f"cube is: {b}")

#     @staticmethod
#     def greet():
#         print("Your code is running fine")   

# y=calculator()              #object creation and storing in a variable
# y.square()
# y.cube()
# y.greet()


# class new:
#     a= 12
#     name= "sarthak"

# obj=new()
# obj.a=0         #instance attribute> class attribute
# print(obj.a)



from random import randint

class Train:

    def __init__(self, trainNo):   #dunder method , it is automatically called
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Siliguri", "Delhi")
t.getStatus()
t.getFare("Siliguri", "Delhi")

