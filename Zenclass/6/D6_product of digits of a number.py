## Program to find product of digits of a number

number = int(input("Enter the number :"))
product = 1
temp = number
while(temp>0):
 digit = temp % 10
 product *= digit
 temp //= 10
print(product)