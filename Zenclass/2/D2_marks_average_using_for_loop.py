marks = []
a = int(input('Enter the number of subjects: '))
for i in range(0,a):
 scores = int(input("Enter the mark %d " %(i)))
 marks.append(scores)
print(marks)
aver = sum(marks) / a
print("The average marks scored is: ",aver)