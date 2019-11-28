## Program to search a word in list

fruits = ["apple","grapes","banana"]

def searchstring(word):
 for i in fruits:
  if(word==i):
   return True
x = input()
searchstring(x)
if searchstring(x):
 print("True")
else:
 print("False")