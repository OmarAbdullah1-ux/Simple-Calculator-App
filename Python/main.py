from calculator import Calculator

def main():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nPlease select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Python Calculator!")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = Calculator.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = Calculator.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = Calculator.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            try:
                result = Calculator.divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()