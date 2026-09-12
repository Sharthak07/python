class Employee:
    company = "ITC"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):  # Programmer inherits Employee
    company = "ITC-Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)


class twoDvector:

    def __init__(self,i,j):
        self.i = i
        self.j = j


    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector):         #inheriting from twoDvector
    def __init__(self, i, j ,k):
        super().__init__(i , j)
        self.k=k


    def show(self):
            print(f"the vector is {self.i}i + {self.j}j + {self.k}k" )


a = twoDvector(1,2)
a.show()
b = threeDvector(1,2,3)
b.show()



class animals:
     a=1

class pets(animals):
     b=2

class dogs(pets):                            # we can add @staticmethod to this as well which does not use object data i.e 'self'
     def bark(self):
        print("example of multilevel inheritance")

o=dogs()
o.bark()


class employee:

    def __init__(self, sal, inc):
        self._sal=sal
        self._inc=0

        self.salaryAfterIncrement = inc  # Calls the setter

    @property                                  # ABSTRACTION: lets us access the calculation simply as an attribute 
    def salaryAfterIncrement(self):            # we can add multiple property if we want as per our need 
        return self._sal + self._inc


    @salaryAfterIncrement.setter                       # A setter is a method that lets you set (assign) the value of a private attribute 
    def salaryAfterIncrement(self,value):             

        if (value > 1000 and value < 5000):            # We can write the same above code just by writing the same logic in @property getter just like below
            self._inc= value
        else:
            print("no increment this time due to performance issues")

a = employee(43000, 1500)
print(a.salaryAfterIncrement)
print(f"the salary is {a._sal} and the increment is {a._inc}")




class employee:                        

    def __init__(self, sal, inc):
        self._sal = sal                # ENCAPSULATION → salary data is stored inside the Employee object
        self._inc = inc                # ENCAPSULATION → increment data is stored inside the Employee object

    @property                          # @property is a decorator that lets you access a method like it's a plain attribute, can return anything
    def salaryAfterIncrement(self):
        # Internal logic is hidden from the user → ABSTRACTION
        if (1000 < self._inc < 5000):
            return self._sal + self._inc
        else:
            return "no increment this time due to performance issues"
 

a = employee(43000, 1500)

print(f"the salary is {a._sal}")
print(a.salaryAfterIncrement)



class Complex:

    def __init__(self, real, imaginary):
        self.real = real             
        self.imaginary = imaginary    


    def __add__(self, other):                               # __add__ is called when we use + between two Complex objects

       new_real = self.real + other.real                    # self.real = c1.real, # other.real = c2.real
       new_imaginary = self.imaginary + other.imaginary     # self.imaginary = c1.imaginary,  # other.imaginary = c2.imaginary

       return Complex(new_real, new_imaginary)              # Create and return a NEW Complex object,  # containing the added values
              

    # Display the complex number
    def show(self):
        print(f"{self.real} + {self.imaginary}i")


# c1 represents 2 + 3i
c1 = Complex(2, 3)

# c2 represents 4 + 5i
c2 = Complex(4, 5)


# c1 + c2 internally calls:
# c1.__add__(c2)
result = c1 + c2

result.show()






