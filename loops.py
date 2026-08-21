# # print odd numbers
# for i in range(1, 20, 2):
#     print(i)


# #print multiplication table of 57
num= 57
for i in range(1,11):
    print(num*i)
print("------done-------------")


# # continue and break
# for i in range(1, 51):
#     if i == 15:
#         continue
#     if i % 3 == 0:
#         print(i)


# to find the first number in range that is divisible by both a and b
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

for num in range(1, 1001):
    if num % a == 0 and num % b == 0:
        print(num)
        break