##Program to print the string to alphabets

string = input("")
string = list(string)
length = len(string)
for i in range(0,length):
 string[i] = string[i].upper()
 name = "".join(string)
print(name)
 
