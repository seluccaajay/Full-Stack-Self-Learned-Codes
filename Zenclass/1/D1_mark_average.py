name = str(input('Enter the name of the student: '))
eng = int(input('Enter the English mark: '))
lang = int(input('Enter the Language mark: '))
phy = int(input('Enter the Physics mark: '))
che = int(input('Enter the Chemistry mark: '))
mat = int(input('Enter the Mathematics mark: '))
total = eng + lang + phy + che + mat
print(total)
percentage = total/500 * 100
print("Your overall percentage is: ", percentage)
seat_eligibility = ((phy + che + mat) / 300 ) * 100
print(seat_eligibility)
if(seat_eligibility>60):
 print("You are eligile for the engineering seat")
 if(seat_eligibility>90):
  print("You are eligile for IIT")
 elif(seat_eligibility>75) and (seat_eligibility<90):
   print("You are eligible for Tier 1 colleges")
  else:
   print("You are eligible for only other colleges")
