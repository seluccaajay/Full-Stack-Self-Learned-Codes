## Program to search all occurence of a character in a given string

string = input("Enter a string: ")
letter = input("Enter the word to find: ")
b = len(string)
list = []
for i in range(0,b):
 if(string[i]==letter):
  list.append(i+1)
print("The character",letter,"occurs in the following places",list)