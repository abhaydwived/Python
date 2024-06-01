num=int(input("Enter a number to Check...."))
prime=True
if num>1:
   for i in range (2,num-1):
       if num%i==0:
        prime = False
        break


print(prime)
    