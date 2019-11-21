A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
pair1 = (A**2 + B**2 + C**2)**2
pair2 = (A**4 + B**4 + C**4)*2
if(pair1>pair2):
 print("yes")
else:
 print("no")
