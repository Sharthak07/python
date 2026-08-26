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


