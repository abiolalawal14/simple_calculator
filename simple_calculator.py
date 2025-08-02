# program simple_calculator.py
def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y
def divide(x, y):
    """Return the quotient of x and y."""   
    if y == 0:
        raise ValueError("Cannot divide by zero.")  
    return x / y
def calculator():
    """Simple calculator function."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")  
    choice = input("Enter choice (1/2/3/4): ")
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation.")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")   
if __name__ == "__main__":
    calculator()
# This code implements a simple calculator that can perform addition, subtraction,
# multiplication, and division. It prompts the user to select an operation and input two numbers,
# then performs the selected operation and displays the result. It also handles invalid inputs and division by zero.