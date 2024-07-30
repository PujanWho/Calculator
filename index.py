### Time Started GMT+5:45 - 13:56 30/07/2024

def add(x, y):
    return print(x + y)

def subtract(x, y):
    return print(x - y)

def multiply(x ,y):
    return print(x*y)

def division(x, y):
    return print(x/y)

def power(x, y):
    return print(x**y)

print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
print("5. Power")
num = int(input("Enter number 1,2,3,4,5: "))

if num == 5:
    num1 = int(input("Enter the number you want to multiply by exponent: "))
    num2 = int(input("Enter the number value for exponent: "))
    power(num1, num2)
else:
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter Second number: "))
    if num == 1:
        add(num1, num2)
    elif num == 2:
        subtract(num1, num2)
    elif num == 3:
        multiply(num1, num2)
    else:
        division(num1, num2)