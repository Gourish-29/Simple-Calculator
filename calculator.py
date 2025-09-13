num1= float(input())
num2= float(input())
operator=input("enter the operation (+ - * /)\n")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(float(num1 / num2))
else:
    print('Invalid operator')