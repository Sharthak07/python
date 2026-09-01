import qrcode

img = qrcode.make("www.example.com")
img.save("qr.png") 

name= "sarthak"
print(name.endswith("k"))

name= "sarthak"
print(name.startswith("t"))

name= "lets not waste time\nand start learning python"
print(name)             #\n, \t, \', \\ is escape sequence for new line

name= "lets not waste time\nand start learning python"
print(name.splitlines()) #The splitlines() method splits a string into a list. The splitting is done at line breaks.

name = input("enter your name: ")
print(f"good morning, {name}")  #Python's way of inserting variables directly into a string called fstring

letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Sarthak").replace("<|Date|>", "24 September 2050"))  # chaining of replace method

l1= [12, 14, 67, 45, 34, 89]
l1.sort()
l1.reverse()
l1.pop()   #pops from the nth index
l1.pop(1)   # pops the exact index number
l1.remove(34)   #pops the given value in list
print(l1)