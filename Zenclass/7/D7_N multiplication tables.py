## Program to print n multiplication tables

n = int(input("Enter a number: "))
j = 1
for j in range(1,n+1):
 for i in range(1,15):
  c = n * i
  print(j, 'x', i, '=', j*i)
