n=int(input("Enter which number factorial you want..."))
t=n
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print('Factorial of' , t ,'=',fact)