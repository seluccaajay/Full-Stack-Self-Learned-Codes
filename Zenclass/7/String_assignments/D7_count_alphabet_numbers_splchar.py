## Program to find total number of alphabets,digits and special characters in a string

string = input("Enter a string: ")
length = len(string)
upper_alphabets = 0
small_alphabets = 0
numbers = 0
special_characters = 0
for i in range(0,length):
 temp = ord(string[i])
 if(temp>48 and temp<58):
  numbers +=1
 elif(temp>64 and temp<91):
  upper_alphabets += 1
 elif(temp>96 and temp<123):
  small_alphabets += 1
 else:
  special_characters += 1
print("The number of digits are: ",numbers)
print("The number of upper case alphabets are: ",upper_alphabets)
print("The number of lower case alphabets are: ",small_alphabets)
print("The number of special characters are: ",special_characters)
  