## Function to replace a letter with another


def ajreplace(string1,character,replacechar):
 string2=''
 res = list(string1) 
 for i in range(0,len(res)):
  if res[i]==character:
   res[i]=replacechar
 string2="".join(res)
 return string2
a=input("enter the string")
c=input("enter the character to be changed")
d=input("enter the replacement character")
x=ajreplace(a,c,d)
print(x)