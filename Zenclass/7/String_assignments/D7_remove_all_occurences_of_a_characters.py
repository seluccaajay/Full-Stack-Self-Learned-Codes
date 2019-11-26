## Program to remove all repeated characters of a string

string=input("Enter the string: ")
alphabet=input("Enter the alphabet to be found:")
count=0
for i in range(0,len(string)):
 if(string[i]==alphabet):
  string2 = string.replace(string[i],"")
print(string2)