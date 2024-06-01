#return vs yeild run kara ke dekhoo
def even(n):
    for i in range (2,n+1,2):
        return i
# for num in even(12):
#     print(num)
print("return wala :",even(12))
print("\n")

def even(n):
    for i in range (2,n+1,2):
        yield i
for num in even(12):
    print("yield wala :",num)
