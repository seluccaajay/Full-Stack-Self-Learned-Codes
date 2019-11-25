## Program to find sum of digits of a number

number = int(input("Enter the number :"))
sum = 0
temp = number
while(temp>0):
 digit = temp % 10
 sum += digit
 temp //= 10
print(sum)