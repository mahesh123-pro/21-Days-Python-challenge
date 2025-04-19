def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    return x/y

print("select operation:")
print("1.add")
print("2.sub")
print("3.multi")
print("4.divide")
choice=input("enter choice(1/2/3/4):")

try:
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    
    if choice=='1':
        print("result:",add(num1,num2))
    elif choice=='2':
        print("result:",sub(num1,num2))
    elif choice=='3':
        print("result:",multi(num1,num2))
    elif choice=='4':
        print("result:",divide(num1,num2))
    else:
        print("invalid input")
except ValueError:
    print("invalid input, please enter a number")