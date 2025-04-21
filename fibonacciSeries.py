n_terms=int(input("Enter the number of terms: "))
#first two terms
a, b = 0, 1
count=0
if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence upto",n_terms,":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a,end=" ")
        nth = a + b
        # update values
        a = b
        b = nth
        count += 1