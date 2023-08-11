print("Let's calculate!")
number1 = float(input("First number: "))
number2 = float(input("Second number: "))
print("What should we do with your numbers?")
operation = input("Operation (+, -, *, /): ")
if operation == "+":
    print("Result: ", number1 + number2)
elif operation == "-":
    print("Result: ", number1 - number2)
elif operation == "*":
    print("Result: ", number1 * number2)
elif operation == "/":
    print("Result: ", number1 / number2)
else:
    print("ERROR: Invalid operation.")
