list = []
even = 0
odd = 0
list1 = []
list2 = []
num = int(input("Enter the number of terms: "))
for i in range(0,num):
 ele = int(input("Enter the elements: "))
 list.append(ele)
for i in list:
 if(i%2==0):
  even += 1
  list1.append(i)
 elif(i%2 == 1):
  odd += 1
  list2.append(i)
print(list1)
print(list2)
