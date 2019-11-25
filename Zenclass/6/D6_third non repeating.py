list1 = []
num = int(input())
count = 0
for i in range(0,num):
 ele = int(input("Enter the elements in list 1: "))
 list1.append(ele)
for j in range(0,num):
 for k in range(0,num):
  if(list1[j]==list1[k]):
   break
 if(k==num):
  print(list1[j])
  print(count)
  count += 1
    
  