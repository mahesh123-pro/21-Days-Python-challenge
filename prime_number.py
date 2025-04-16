# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print all prime numbers up to 'n' and their sum
def sum_of_prime(n):
    prime_number = []
    total_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            prime_number.append(num)
            total_sum += num

    print("Prime numbers up to", n, "are:")
    print(prime_number)
    print("Sum of prime numbers:", total_sum)

# Get input from the user for summing primes
try:
    user_input = int(input("Enter a number to find all primes up to it: "))
    sum_of_prime(user_input)
except ValueError:
    print("Please enter a valid number.")

# Get input from the user to check if a number is prime
try:
    num = int(input("Enter a number to check if it is prime: "))
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is NOT a prime number.")
except ValueError:
    print("Please enter a valid number.")
