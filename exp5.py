def safe_division():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Please enter a non-zero denominator.")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")
    else:
        print(f"Result: {result}")
    finally:
        print("Program execution completed.")

safe_division()
