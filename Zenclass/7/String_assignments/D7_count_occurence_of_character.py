## Program to count occurence of a character in a string

string=input("Enter the string: ")
alphabet=input("Enter the alphabet to be found:")
count=0
for i in range(0,len(string)):
 if(string[i]==alphabet):
  count+=1
print("The number of times  " ,alphabet," occured in string is: ",count)