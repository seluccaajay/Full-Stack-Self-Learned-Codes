## Program to enter a number and reverse it

num=int(input("Enter a number: "))
temp=num
reverse=0
while(temp>0):
    a=temp%10
    reverse=reverse*10+a
    temp=temp//10
print("The reversed number is: ",reverse)