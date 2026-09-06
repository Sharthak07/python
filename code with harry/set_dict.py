dict= {

        "jaldi": "the late",
        "wait"  : "ruko"
    }
x= input("enter the hindi word: ")
print(dict[x])


numbers = input("Enter four numbers separated by space: ").split(' ')
numbers = set(numbers)
print("Unique numbers:", numbers)


s = set()
s.add(20)
s.add(20.0)
s.add('20')  # length of s after these operations?
print(len(s))


d= {}
key= input("enter four friends name: ").split(' ')
value= input("enter friends number: ").split(' ')       #cannot use 'list' as a dict key (unhashable type: 'list') so zip() stitches two lists together pair by pair
d = dict(zip(key, value))   
print(d)


s={8,7,12,"Harry",[1,2]}   
print(s, type(s))    