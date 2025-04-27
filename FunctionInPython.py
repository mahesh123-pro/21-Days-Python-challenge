# def greet(name):
#     print(f"Hello, {name}! Welcome to my portfolio.")
# name=input("Enter your name sir: ")

# #calling the user-defined function
# greet(name)
# print("\n----------------------------------------------------\n")

def add_numbers(a, b):
    return a+b
def sub_numbers(a, b):
    return a-b
def mul_numbers(a, b):
    return a*b

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

result=add_numbers(a, b)
print("sum of the 'a' and 'b' is: ",result)

result=sub_numbers(a, b)
print("subtraction of the 'a' and 'b' is: ",result)

result=mul_numbers(a, b)
print("multiplication of the 'a' and 'b' is: ",result)