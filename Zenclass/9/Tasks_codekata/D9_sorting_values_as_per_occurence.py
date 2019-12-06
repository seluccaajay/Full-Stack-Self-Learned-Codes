## Program to print the numbers in a list according to the highest occurence of it

list = []
n = int(input("Enter the no of values in list: "))
for i in range(0,n):
 ele = int(input("Enter the elements: "))
 list.append(ele)
print(list)
final = {}
count_list = []
for i in range(0,len(list)-1):
 count = 1
 for j in range(i+1,len(list)):
  if(list[i]==list[j]):
   count += 1
 count_list.append(count)
print(count_list)
   