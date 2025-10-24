def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Try again.")
                continue

            print("Result:", result)
            
            next_calc = input("Do you want to calculate again? (yes/no): ").lower()
            if next_calc != 'yes':
                print("Calculator closed.")
                break

        except ValueError:
            print("Invalid input! Please enter numbers only.")

calculator()