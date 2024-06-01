n=int(input("Enter which Table you want..."))
for i in range(1,11):
    multiplication=n*i
    if i==5:
        continue
    print(n,"x",i,"=",multiplication)