## Program to print the below pattern


list=[1,2,3,4,5]
for i in list:
 if int(i)%2==0:
   for j in range(0,int(i)):
    j="*"
    print(j,end="")
 else:
    for j in range(0,int(i)):
     j="+"
     print(j,end="")
 print('\r')