## Tuples are entered in a simple paranthesis

marks = (100, 30, 70, 80, 70, 50, 40, 60, 80, 50)

## If we need to check for how much time has a value been repeated inside a tuple, then we can use count function

x = marks.count(5)
print(x)

## To search the index of the value that occurs for a first time in a tuple can be done

x = marks.index(80)
print(x)

## Accessing a tuple as similar in a list. (Positive and Negative Indexing)

fruits = ("apple","banana","orange","kiwi","dragon fruit","jack fruit","pomegranate","tomato")
print(fruits[0])
print(fruits[-2])

## We can also print from one value to another value (range of values) in a tuple (positive and negative indexing)

print(fruits[2:5])

## Changing the values is not possible, but if you want to change a value, you can convert a tuple to a list and then
## (contd) convert it to a tuple after changing the value.

new_fruits =("apple","banana","orange")
y = list(new_fruits)
y[1] = "kiwi"
new_fruits = tuple(y)
print(new_fruits)

## As similar to a list, if we need to print only the values one by one we can do it as a for loop

for e in new_fruits:
 print(e)
 
## We can also check whether the value is present in list or not.

if "apple" in new_fruits:
 print("yes, Apple is there in new fruits")
 
## To find a length of a tuple.

a = len(new_fruits)
print(a)

## Adding new items  or removing an item into/from a tuple is not possible.

## Creating a tuple with one items

marks1 = (1,)
print(marks1)

marks2 = (1)
print(marks2)

## Similar to list we can use + to concat two strings

total = fruits + new_fruits
print(total)






