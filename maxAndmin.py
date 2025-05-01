def find_max_min():
    data = input("Enter the numbers separated by space: ")
    try:
        numbers = list(map(int, data.split()))

        if not numbers:
            print("No numbers were entered.")
            return

        max_val = max(numbers)
        min_val = min(numbers)

        print(f"Maximum value: {max_val}")
        print(f"Minimum value: {min_val}")

    except ValueError:
        print("Please enter valid numbers separated by space.")

find_max_min()
