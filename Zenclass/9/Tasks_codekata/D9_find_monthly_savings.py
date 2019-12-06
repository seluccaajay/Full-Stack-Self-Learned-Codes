## Program to find monthly savings

month = [1000]
n = int(input())
savings = 1000
if(n==1):
  print(savings+savings)
if(n==0):
  print(savings)
elif(n>1):
  for i in range(1,n+1):
    month.append(savings)
  print(sum(month))
  
  
