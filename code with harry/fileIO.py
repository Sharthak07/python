file = open("file.txt", "r")

for line in file:
    print(line, end="")

file.close()


f= open("file.txt")  #open a file in read mode, 'r' is default mode, so we can skip it
data= f.read()
print(data)
f.close()


text = "sarthak is a good boy"

f= open("file.txt", 'w')
f.write(text)
f.close()



f= open("file.txt")         #check given word is present in file or not
data= f.read()
x=input("enter a word to check if it is present in the file or not: ").lower()
if x in data:
    print("yes, entered word is present in the file")
else:
    print("wrong word entered, word not present in the file")
f.close()



# game function 
import random

def game():  #defining func
    lucky_no = random.randint(1, 100) 

    attempts= 0
    while True:
        no_of_guess= int(input("Enter your guess: "))
        attempts+=1
        if (no_of_guess == lucky_no):
            print("Congratulations! You guessed the lucky number.")
            break
        elif no_of_guess < lucky_no:
            print("Your guess is too low. Try again.") 
        else:
            print("Your guess is too high. Try again.") 
    return attempts

    
#main logic(file read and write)
with open("high_score.txt", "r") as f:
    content = f.read()

if content == "":
    old_score = float('inf')  # no previous record, cannot do int('inf') here as int() can only turn things like "5", "42" into numbers.It has no meaning with the letters
else:
    old_score = int(content)

no_of_attempts =game()  #calling func
print(f"Number of attempts: {no_of_attempts}")

if no_of_attempts < old_score:
    with open("high_score.txt", "w") as f:
        f.write(str(no_of_attempts))
    print("New High_score!", no_of_attempts)
else:
    print("No new record. Hi-score remains:", old_score)





import os

os.makedirs("mul_tables", exist_ok=True) # create a new folder
for i in range(2,11):                    # outer loop for multiplication tables from 2 to 10
    filename= f"mul_tables/mul_table_{i}.txt"

    with open(filename, "w") as f:
        for j in range(1,11):           #inner loop for multiplication table of a number
            line= f"{i} x {j} = {i*j}\n"
            f.write(line) 



#replace all occurrences of a word in a file with another word
with open("donkey.txt", "r") as file:
    data=file.read()

content= data.replace("donkey","######")        # The replace() method finds and replaces text in a string

with open("donkey.txt", "w") as file:
    file.write(content)



words_to_censor = ["donkey", "idiot", "stupid"]  # <-- you define this list

with open("file.txt", "r") as file:
    content = file.read()

for word in words_to_censor:                    #same program, used for loop to iterate through the list of words to censor
    content = content.replace(word, "######")

with open("file.txt", "w") as file:
    file.write(content)



with open("file.txt", "r") as file:
    data = file.read()

if "wonder" in data:
    print("Yes, 'wonder' is present in the file")
else:
    print("No, 'wonder' is not present in the file")



with open("log.txt", "r") as file:
    lines = file.readlines()

line_no=1
for line in lines:
    if ("python" in line):
        print(f"Yes, python is present in the file,{line_no}")
        break          # Exit the loop immediately (stop searching)
    line_no+=1

else:                        # This else runs ONLY if the loop completes WITHOUT hitting break (meaning "python" was NOT found in any line)
    print("No, python is not present in the file")   




try:
    with open("abc.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")



#wipe out file content
with open("log.txt", "w") as file:
    file.write("")                 



 #used for renaming a file
with open("old.txt") as f:
    content = f.read()         

with open("renamed_by_python.txt", "w") as f:
    f.write(content)