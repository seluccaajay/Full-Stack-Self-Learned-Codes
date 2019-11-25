## Program to print all the even numbers between 1 to 100


even_numbers = []
i = 1
while(i<=100):
 if(i%2 == 0):
  even_numbers.append(i)
 i += 1
print(even_numbers)