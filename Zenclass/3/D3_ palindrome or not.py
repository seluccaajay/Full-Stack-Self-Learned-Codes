

string=str(input("Enter the String:"))
l=len(string)
flag=0
for i in range(l//2):
 if( string[i]!=string[l-i-1]):
  flag=1
  break
if flag==1:
 print("Not Palindrome")
else:
 print("Palindrome")

