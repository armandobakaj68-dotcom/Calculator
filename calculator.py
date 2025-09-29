import math

operator = input("Enter an operator (+ - * / ^ √):")
if operator == "√":
    num = float(input("Enter a number: "))
else:    
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))


if operator == "/":
    if num2 == 0:
        print("Unavailable: Division by zero")
    else:
     rezult = num1 / num2
     print(rezult)
elif operator == "√":
   rezult = round(math.sqrt(num), 2) 
   print(rezult)    
elif operator == "+":
    rezult = num1 + num2
    print(rezult)
elif operator == "-":
    rezult = num1 - num2
    print(rezult)
elif operator == "*":
    rezult = num1 * num2
    print(rezult)

elif operator == "^":
    rezult = pow(num1, num2)
    print(rezult)
else:
    print("Unavailable operator")
