## Program to find Least Common Multiple of two numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if(num1>num2):
 greater = num1
else:
 greater = num2
while(True):
 if((greater%num1==0) and (greater%num2==0)):
  lcm = greater
  break
 greater += 1
print(greater)

