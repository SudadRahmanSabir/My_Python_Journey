# Simple Calculator with Modular Design
from simple_calculator import add, subtract, multiply, divide, square_root, power, clear

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Clear")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", add(a, b))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '2':
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", subtract(a, b))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '3':
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", multiply(a, b))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '4':
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", divide(a, b))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '5':
            try:
                a = float(input("Enter number: "))
                print("Result:", square_root(a))
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '6':
            try:
                a = float(input("Enter base number: "))
                b = float(input("Enter exponent: "))
                print("Result:", power(a, b))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '7':
            print("Result:", clear())
        elif choice == '8':
            print("Goodbye! Thanks for using the calculator.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()




