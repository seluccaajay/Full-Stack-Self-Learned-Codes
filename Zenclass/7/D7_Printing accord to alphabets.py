## PROGRAM TO PRINT 8 NUMBERS ALONG WITH THE ALPHABETS

alphabet = str(input("Enter an alphabet: "))
ascii = ord(alphabet)
for i in range(65,ascii+1):
 print(chr(i),"", end = "")
 for j in range(1,9):
  print(j, end =" ")
 print('\r')