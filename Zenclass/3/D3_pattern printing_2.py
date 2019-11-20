## PRINTING THE INCREMENTING PATTERN

##  *
##  **
##  ***

## The pattern has no space in the middle and also in front of the star

temp = 3  ## as there are 3 rows in the pattern
for i in range(0,temp):
 for j in range(0,i+1):
  print("*",end="")
  j += 1
 print('\r')
 i += 1

## PRINTING THE DECREMENTING PATTERN

##  ***
##  **
##  *

## The pattern has no space in the middle and also in front of the star

temp = 3  ## as there are 3 rows in the pattern
for i in range(0,temp):
 for j in range(0,temp-i):
  print("*",end="")
  j += 1
 print('\r')
 i += 1