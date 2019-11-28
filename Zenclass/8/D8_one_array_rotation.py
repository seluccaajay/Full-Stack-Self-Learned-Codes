## Program to write array rotation

list1 = [5,6,7,8]
n = int(input())
for i in range(0,n):
 temp = list1[0]
 for i in range(0,len(list1)-1):
  list1[i]=list1[i+1]
 list1[i+1]=temp
 print(list1)
 
n = input()
listone = []
listone = input().split()
listtwo = []
listtwo = input().split()
