def product(list):
    p=1
    for i in list:
        p*=i
        print(p)
    return p
arr=[3,4,5,6,7,8,9,10,11,12,]
c=product(arr)
print("Cummulative product of the list is::",c)