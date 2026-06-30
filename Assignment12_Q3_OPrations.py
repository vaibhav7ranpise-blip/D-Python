Addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: Division by zero"


def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
           RData = Addition(num1, num2)
           print("Addition is: ",RData)
        elif choice == '2':
            RData = subtraction(num1, num2)
            print("Subtraction is: ",RData)
        elif choice == '3':
            RData = multiplication(num1, num2)
            print("Multiplication is: ",RData)
        elif choice == '4':
            RData = division(num1, num2)
            print("Division is: ",RData)
    else:
        print("Invalid input") 

if __name__ == "__main__":
    main() 
