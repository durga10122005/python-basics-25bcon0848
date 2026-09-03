def factorial(n):
    """
    Recursive function to calculate the factorial of a non-negative integer.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    print("--- Factorial Calculator ---")
    
    try:
        # Take integer input from the user
        user_input = int(input("Enter a non-negative integer: "))
        
        # Check if the number is negative
        if user_input < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            # Calculate and display the result
            result = factorial(user_input)
            print(f"The factorial of {user_input} is: {result}")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid whole number.")


if __name__ == "__main__":
    main()
