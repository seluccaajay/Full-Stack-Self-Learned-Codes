## Program to write a great number

N = input()
N = int(N)
first_digit = N//10
last_digit = N%10
sum = first_digit + last_digit
product = first_digit * last_digit
total = sum + product
if(total == N):
 print("great")
else:
 print("none")