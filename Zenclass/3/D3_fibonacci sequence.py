terms = int(input("Enter the number of terms: "))
n1,n2 = 0,1
order = 0
if(terms <= 0):
 print("Enter a positive number")
elif(terms == 1):
 print("The sequence is: ")
 print(n1)
else:
 print("Fibonacci Sequence is: ")
 while(order<terms):
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  order += 1