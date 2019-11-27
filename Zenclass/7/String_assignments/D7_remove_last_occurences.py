## Program to remove last occurences of a char with another

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
string2 = ''
length = len(string)
for i in range(length):
 if(string[i] == char):
  string2 = string[0:i] + string[i + 1:length] 
print("Original String :  ", string)
print("Final String :     ", string2)