import statistics

def main():
    # Input: take a list of numbers from the user
    data = input("Enter numbers separated by spaces: ")
    
    # Convert the input string to a list of floats
    numbers = list(map(float, data.split()))

    # Check if the list is empty
    if not numbers:
        print("No data entered!")
        return

    # Mean
    mean_value = statistics.mean(numbers)
    print(f"Mean: {mean_value}")

    # Median
    median_value = statistics.median(numbers)
    print(f"Median: {median_value}")

    # Mode (handle case where mode may raise an exception if no unique mode exists)
    try:
        mode_value = statistics.mode(numbers)
        print(f"Mode: {mode_value}")
    except statistics.StatisticsError as e:
        print(f"Mode: {e} (no unique mode)")

# Run the program
main()
