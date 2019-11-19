## LIST IN PYTHON similar TO ARRAYS

## Defined in square braces

## Creating a simple list

list1 = [1,2,3,4,5,6,7,8,9]
print(list1)

## Accessing items using positive and negative indexing

print(list1[0])
print(list1[-3])

## Range Indexing (printing a range of variable from a list)

print(list1[0:4])

## Change the item in a list

list1[4] = 56
print(list1)

## to print the values in a list one by one

for x in list1:
 print(x)

## To check whether the item exists in a list

if 2 in list1:
 print("You have the number you want!")
 
## we can use append function to add a value in a list at the last

list1.append(5)
print(list1)

## we can also use insert fn to insert a value at user defined index

list1.insert(5, 1886)
print(list1)

## we can use reverse fn to reverse a complete list

list1.reverse()
print(list1)

## We have pop fn to remove the last item by default and also remove fn to remove a particular value

list1.remove(1886)
print(list1)
list1.pop()
print(list1)

## index fn can be used to find the index position of the particular value

a = list1.index(2)
print(a)
