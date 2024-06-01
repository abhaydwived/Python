# kitne bhi parameter ya arguments ke liye *agrs ka use krte hai specially tabh use krte ahi jab kitne parametres hai ye pata na hoo
def sum_all(*args):
    print(*args)

    return sum(args)
print(sum_all(1,2,3,4,5,6,7,8,9))
