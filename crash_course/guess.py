import random


def guess_number():  #defining func
    lucky_no = random.randint(1, 50) 


    while True:
        no_of_guess= int(input("Enter your guess: "))
        if no_of_guess == lucky_no:
            print("Congratulations! You guessed the lucky number.")
            break
        elif no_of_guess < lucky_no:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.") 


guess_number()  #calling func


# name = input("Enter your name: ")
# print(name[::-1])


