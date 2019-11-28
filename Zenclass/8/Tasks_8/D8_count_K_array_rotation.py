## Program to find count k by which the array has been rotated

n = input()
list1 = []
list2 = []
list1 = input().split()
list2 = input().split()
length = len(list1)
length2 = len(list2)
if(length ==length2):
 for i in range(0,length):
  for j in range(0,length2):
   if(list1[i]==list2[j]):
    rotate = length2 - j
 print(rotate-1)