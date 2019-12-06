## Program to check wave array or not

array = [0,1,2,3,4,5,6,7]
sum =0
for i in range(0,len(array),2):
 if(array[i]%2==0):
  sum = sum + array[i]
print(sum)
 
