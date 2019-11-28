## Implementing a function to check all the letters are upper case

def isnewupper(val):
 length = len(val)
 count = 0
 for i in range(0,length):
  temp =ord(val[i])
  if(temp>=65 and temp<=90):
   count += 1
 if(count==length):
   return True
x = input()
if isnewupper(x):
 print("True")
else:
 print("false")
  
  