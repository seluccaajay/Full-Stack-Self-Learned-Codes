## Program to count frequency of each character in a string

string = input("Enter a string: ")
frequency = {}
for i in string: 
 if(i in frequency): 
  frequency[i] += 1
 else: 
  frequency[i] = 1
print("The characters and respective counts are as follows")
print(str(frequency))