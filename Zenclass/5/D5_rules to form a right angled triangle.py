## PROGRAM TO CHECK WHETHER THE VALUES ARE ELIGIBLE TO FORM SIDES OF A RIGHT ANGLED TRIANGLE


A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if(C**2 == A**2 + B**2):
 print("Yes, the values can form a right angled triangle")
else:
 print("No, the values entered do not satisfy rules to for a right angled triangle")
