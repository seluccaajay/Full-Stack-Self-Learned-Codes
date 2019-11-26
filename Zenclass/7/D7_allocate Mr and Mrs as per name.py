names = ["Arun","Akshaya","Devi","Ajay"]
gender = ["M","F","F","M"]
for i in range(0,len(names)):
 if(gender[i]=='M'):
  print('Mr.',names[i])
 elif(gender[i]=='F'):
  print('Ms.',names[i])