string=input("Enter a stirng...")
for char in string:
    if string.count(char)==1:
        print("first non repeated letter is ",char)
        break

