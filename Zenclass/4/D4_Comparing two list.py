list1 = []
list2 = []
num = int(input("Enter the number of terms in list1: "))
num1 = int(input("Enter the number of terms in list2: "))
for i in range(0,num):
 ele = int(input("Enter the elements in list 1: "))
 list1.append(ele)
for j in range(0,num1):
 ele2 = int(input("Enter the elements in list 2: "))
 list2.append(ele2)
print(list1)
print(list2)
if (list1 == list2):
 print("Same")
else:
 print("different")

