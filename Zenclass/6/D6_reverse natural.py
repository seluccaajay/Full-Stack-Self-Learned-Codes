## Program to print all the natural numbers from reverse

n = int(input("Enter the number of natural no's you want: "))
natural_numbers=[]
while(n>=1):
 natural_numbers.append(n)
 n -= 1
print(natural_numbers)