num=int(input("Enter the your armstrong number: "))
orignial = num
sum =0
n=len(str(num))
while num>0:
    digit=num%10
    sum=sum+(digit**n)
    num=num//10
    
if sum==orignial:
    print("The number is armstrong")
else:
    print("The number is not armstrong")