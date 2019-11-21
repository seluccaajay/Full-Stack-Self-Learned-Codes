## Write a program to convert the list x as mentioned below
## x = ['a','e','m','r']  to ['b','f','n','s']

x = ['a','e','m','r']
z = []
length = len(x)
for i in range(0,length):
 y = chr(ord(x[i])+1)
 z.append(y)
 i += 1
print(z)
 