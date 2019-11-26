

string=str(input("Enter the String:"))
l=len(string)
a=0
for i in range(l//2):
 if( string[i]!=string[l-i-1]):
  a=1
  break
if a==1:
 print("Not Palindrome")
else:
 print("Palindrome")

    