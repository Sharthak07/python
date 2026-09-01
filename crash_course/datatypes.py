# marks= {101,105,102,101,108,105,110}
# print (marks, type(marks))

# tuples in list
employee= [(101,"aline",50000),(102,"bob",60000),(103,"charlie",70000)]
a= int(input("Enter the id: "))
for item in employee:
    if item[2] == a:
        print(item)
        break
else:
    print("id not found")



# find avg from list of marks in parameter
def avg_func(marks=(12,14,16,18,20,25,30)):
    avg_cal= round(sum(marks)/len(marks), 3)
    return avg_cal

average= avg_func()
print(average)
