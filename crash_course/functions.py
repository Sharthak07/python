
# def even_odd(num):           #function define
#     if num % 2 == 0:
#         print("even no")
#     else:
#         print("odd no")


# even_odd(14)                #function call


# count vowels in string passed as arguement
# def count_vowels(s):
#     count = 0
#     for char in s:
#         if char in "aeiouAEIOU":
#             count = count + 1
#     return count

# result = count_vowels("ironman")
# print(result)


# function to return prime number or not
def prime(num):
    count=0
    for i in range(1, num+1):
        if num%i == 0:
            count+= 1

    if count == 2:
        print("prime number")
    else:
        print("not prime number") #function define
    

prime(2)























