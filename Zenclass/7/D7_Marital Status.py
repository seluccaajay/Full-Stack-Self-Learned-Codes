## Program to allocate  and remove Marital Status

names = ["Arun","Akshaya","Devi","Ajay"]
gender = ["M","F","F","M"]
status = ["M","S","M","S"]
for i in range(0,len(names)):
 if(gender[i]=="M"):
  print("Mr.",names[i])
 elif(gender[i]=="F" and status[i]=="M"):
  print("Mrs.",names[i])
 elif(gender[i]=="F" and status[i]=="S"):
  print("Ms.",names[i])

x = ["Mr.Arun","Ms.Akshara","Mrs.Devi","Mr.Ajay"]
for i in range(len(x)):
 pos = x[i].index('.')
 str = x[i]
 x[i]=str[pos+1:]
print(x) 