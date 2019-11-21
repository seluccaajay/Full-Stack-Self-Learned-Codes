list1 = []
unique_list = []
num = int(input("Enter the number of terms in a list: "))
for i in range(0,num):
 ele = int(input("Enter the elements: "))
 list1.append(ele)
print(list1)
for a in list1:
 if a not in unique_list:
  unique_list.append(a)
print(unique_list)