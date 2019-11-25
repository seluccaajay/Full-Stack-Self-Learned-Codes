## Program to print all the odd numbers between 1 to 100
odd_numbers = []
for i in range(1,101):
 if(i%2 != 0):
  odd_numbers.append(i)
print(odd_numbers)