#Initialize array     
list1 = [];
duplicate_elements = []
terms = int(input("Enter the number of terms in list: "))
for k in range(0,terms):
 ele = int(input('Enter the elements of list1: '))
 list1.append(ele)   
print("Duplicate elements in given array: "); 
for i in range(0, len(list1)):    
 for j in range(i+1, len(list1)):    
  if(list1[i] == list1[j]):    
   duplicate_elements.append(list1[j])
print(duplicate_elements)
