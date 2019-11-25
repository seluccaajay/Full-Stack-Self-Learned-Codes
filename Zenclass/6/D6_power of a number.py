## Program to find the power of a number using for loop

n = int(input("Enter the number: "))
order = int(input("Enter the power: "))
temp = 0
for i in range(1,order+1):
 temp = n ** i
print(temp)
 