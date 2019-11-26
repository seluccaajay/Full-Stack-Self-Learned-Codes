## Program to find total number of vowels and consonants in a string

string = input("Enter a string: ")
length = len(string)
consonants = 0
vowels = 0
for i in range(0,length):
 temp = ord(string[i])
 if(temp==65 or temp==97 or temp==69 or temp==101 or temp==73 or temp==105 or temp==79 or temp==111 or temp==85 or temp==117):
  vowels += 1
 else:
  consonants += 1
print("The number of vowels in the string is: ",vowels)
print("The number of consonants in the string is: ",consonants)  
  