starting_km = int(input('Enter the Starting Km :'))
ending_km = int(input('Enter the ending km: '))
total_distance = ending_km - starting_km
if(total_distance>5):
 basic_fare = ((total_distance - 5)*8) + 100
else:
 basic_fare = 100
peak_time = int(input('Enter 1 for peak time and 0 for normal time'))
if(peak_time == 1):
 total_fare = basic_fare + ( 0.25 * basic_fare)
 print('Your total fare is : ', total_fare)
else:
 print('Your total fare is : ', basic_fare)