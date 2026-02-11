import math

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero."
    return a % b

def floor_division(a, b):
    if b == 0:
        return "Error! Floor division by zero."
    return a // b

def square_root(a):
    if a < 0:
        return "Error! Cannot take square root of negative number."
    return math.sqrt(a)


while True:
    print("\n===== SMART CALCULATOR V2 =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root (√)")
    print("9. View History")
    print("10. Clear History")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == '11':
        print("Thank you for using Smart Calculator V2!")
        break

    elif choice == '9':
        print("\n--- Calculation History ---")
        if history:
            for item in history:
                print(item)
        else:
            print("No history available.")

    elif choice == '10':
        history.clear()
        print("History cleared successfully.")

    elif choice in ['1','2','3','4','5','6','7']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                expression = f"{num1} + {num2} = {result}"

            elif choice == '2':
                result = subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"

            elif choice == '3':
                result = multiply(num1, num2)
                expression = f"{num1} * {num2} = {result}"

            elif choice == '4':
                result = divide(num1, num2)
                expression = f"{num1} / {num2} = {result}"

            elif choice == '5':
                result = power(num1, num2)
                expression = f"{num1} ^ {num2} = {result}"

            elif choice == '6':
                result = modulus(num1, num2)
                expression = f"{num1} % {num2} = {result}"

            elif choice == '7':
                result = floor_division(num1, num2)
                expression = f"{num1} // {num2} = {result}"

            print("Result:", result)
            history.append(expression)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    elif choice == '8':
        try:
            num = float(input("Enter number: "))
            result = square_root(num)
            expression = f"√{num} = {result}"
            print("Result:", result)
            history.append(expression)

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    else:
        print("Invalid choice! Please select between 1-11.")
