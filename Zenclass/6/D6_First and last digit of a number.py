## Program to find first and last digit of a number

n = int(input("Enter a number: "))
last_digit = n%10
print("Last digit of a number is: ",last_digit)
while(n>=10):
 a = n//10
 n = n//10
print("The first digit is : ", a)
 