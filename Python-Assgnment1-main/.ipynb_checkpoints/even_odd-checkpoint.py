# Taking two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking the parity of the numbers
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even, and the other is odd.")
