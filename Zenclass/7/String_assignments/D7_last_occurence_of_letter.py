## Program to find last occurence of a character in a given string

string = input("Enter a string: ")
letter = input("Enter the word to find: ")
b = len(string)
for i in range(0,b):
 if(string[i]==letter):
  a = i
print(a+1)