print('Program to check greatest of three numbers')
first_number = int(input('Enter the First number: '))
second_number = int(input('Enter the second number : '))
third_number = int(input('Enter the third number: '))
if( first_number > second_number):
 if( first_number > third_number):
  print('Greatest Number is : ', first_number)
 else:
  print('Greatest Number is : ', third_number)
else:
 if( second_number > third_number):
  print('Greatest Number is: ', second_number)
 else:
  print('Greatest Number is: ', third_number)