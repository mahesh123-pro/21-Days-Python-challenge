def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.
    
    :param principal: Initial amount of money (P)
    :param rate: Annual interest rate in percentage (R)
    :param time: Time in years (T)
    :param n: Number of times interest is compounded per year
    :return: Compound interest and total amount
    """
    # Convert annual rate from percentage to decimal
    rate = rate / 100

    # Compound Interest Formula: A = P * (1 + R/n)^(n*T)
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal

    return compound_interest, amount

# Example usage
P = float(input("Enter the principal amount (P): "))
R = float(input("Enter the annual interest rate (R) in %: "))
T = float(input("Enter the time in years (T): "))
N = int(input("Enter the number of times interest is compounded per year (n): "))

ci, total_amount = calculate_compound_interest(P, R, T, N)

print(f"\nCompound Interest: ₹{ci:.2f}")
print(f"Total Amount after {T} years: ₹{total_amount:.2f}")
