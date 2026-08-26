python is a case sensetive language

print() is the built-in output fuction we use to display output on screen

variables are the containers we use o store any values inside it

we do not have to explicity type the datatype of a variable in python like c or java

primitive datatypes are str, int, float, bool(True, False)

take the user input and store in variable, x= input("enter your name: ")

every time by default when take input from input() function it stores in the form of string

Type casting changes a value from one data type to another done explicitly by coder, type conversion is done automamatically by interpreter, for eg- print(1+2.5), result will be in float i.e 3.5

if we are assigning string try to assign within "" and single charecters in '', some good conventions to follow and also follow the indentation which is neccesary for clean error free code, follow commenting as well

Strings are immutable in nature, if we change it a new string will be created but the original string will remain the same string opertions: print(name.upper()) an print print(name.lower())

find(): function is used to return index of a string, index is nothing but the char stored in position starting from index[0], if it return -1 it means invalid value means that value entered in print() does not exists

replace(): replacing string value with the original one, eg: print(name.replace("xyz"))

name= "Sarthak" , to check the presence print('S' in name), this will return True

reserved words or keywords are already defined in python so we cannot use those in the form or variables or function names, eg: True, False, None, and, or, not, for, while , break , continue etc etc.

operator precedence () > ** >> +x and -x >> * and / and % >> + -

comparison operators: ==, !=, >, <, >=, <= 

logical operators: AND, OR , NOT........or gives true when either or statement is true. and is the opposite


Conditional staements: Python checks conditions from top to bottom and runs only the first matching block.
age = int(input("Enter your age: "))
    if age > 90:
        print("You are over the allowed age.") #these are called suite
    elif age >= 18:
        print("You can drive.")
    else:
        print("You cannot drive.")


range() generates a sequence of numbers, commonly used with loops, SYNTAX: range(start, stop, step)
>>> start is included
>>> stop is excluded
>>> step control the differnce between numbers

A while loop repeats a block of code while its condition is true

i = 1
    while i <= 5:
    print(i * "*")
    i += 1

Updating the loop variable is important. Without i=i+1, the condition will always remain true which creates infinite loop

print(i * "*") how this is working? basically int getting be multiplied by a string(which logically we cant), that many times he strings repeats i.e everytime i value is getting incremented that many no of * is getting printed in the output

to iterate through sequence of numbers and list(called traversing) we generally use 'for' loops, there must an iterator/ counter variable mst be present

complex or non primitive datatypes are: list, tuple, set, dictionary

list: collection of different items enclosed by [] square brackets, not nesecary the type will be same , means float, int string anything can be stored for eg marks= [98, 99, 97, 95, "A", 93.5] and also list are mutable

marks = [98, 99, 97, 95, 93]
print(len(marks)) to return total no of items in list, also list works on indexed value, eg print(marks[1]), o/p= 99

when we want to print the last index we can start with -1 that is the reverse order we can do -1, -2 and so on

Slicing extracts part of a list
print(marks[0:3])     # [98, 99, 97]   list(list[st:end])  where end index is exclusive in nature
print(marks[-3:-1])     # [97, 95]
print(marks[-3:])       #[97, 95, 93]

append() function adds an element at the end 
marks.append(50)             # marks= [98, 99, 97, 95, 93, 50]

insert() adds an element at a particular position 
marks.insert(0, 50)   ##adding 100 in 0th index, change the index to add the element accordingly
print(marks)           op: [50, 98, 99, 97, 95, 93]

print(95 in marks)  # True                                  
print(100 in marks)  # False

marks.clear()
print(marks)      # []
print(len(marks)) # 0

Tuple: tuples are immmutable, if you need to modify it, you have to create a new tuple. enclosed by () though not mandate, also tuple object does not support item assignment.

We can use tuples inside a list in comma separeted way for eg: employee= [(101,"aline",500),(102,"bob",600),(103,"charlie",700)]
in such case we can use for loop and an iterator to traverse though items or indexes to return the desired value

set: unique collection of values , enclosed by {}, do not store duplicate items by default

dictionary: its a collection of key value pairs, we do not have index in a dictionary instead we use the key to display output, also it accepts duplicates and it is mutable
 
immutable datatypes are faster in memory operations as there is no modification addition 

A function is a reusable block of code that performs a task. Python function names normally use lowercase letters and underscores, such as new_price. We use function to remove redundancy in a code

An argument is the actual value passed while calling the function. A parameter is a variable written in the function definition. we can 'return' only one single value in a function and returned value can be directly printed or can be stored and then printed in the next lines of codes. A returned value can be used in another calculation

## Python Built-in Functions

| Function  | Purpose                              |
|-----------|---------------------------------------|
| `print()` | Displays output                      |
| `input()` | Takes user input                     |
| `len()`   | Returns the number of elements       |
| `type()`  | Returns the data type                |
| `int()`   | Converts a value into an integer     |
| `float()` | Converts a value into a float        |
| `str()`   | Converts a value into a string       |
| `max()`   | Returns the largest value            |
| `min()`   | Returns the smallest value           |
| `sum()`   | Returns the total of numeric values  |

A module is a file containing useful functions and other Python code. Python's math module provides mathematical functions

import math
print(math.sqrt(16))  # 4.0
print(math.log2(64))  # 6.0

dir() displays the names available inside a module





