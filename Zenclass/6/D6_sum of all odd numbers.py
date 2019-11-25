## Program to print sum of odd numbers from 1 to numbers

a = 0
n = int(input("Enter the number of terms: "))
for i in range(1,n+1):
 if(i%2 != 0):  
  a = a + i
print(a)