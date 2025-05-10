def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)
# Test the function
n=int(input("Enter a number to calculate its factorial: "))
print(f"the factorial of {n} is {factorial(n)}")