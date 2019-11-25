## Program to find a factorial of a number

number = int(input("enter the number: "))
factorial = 1
for i in range(1,number+1):
 factorial *= i
print(factorial)