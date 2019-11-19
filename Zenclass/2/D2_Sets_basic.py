processor = {"Intel I5", "Intel I3", "Intel I7"}
print(processor)

## To print the elements in a set as a single value

for x in processor:
 print(x)


##adding an element

processor.add("Intel I9")
print(processor)

## updating an element

processor.update(["INTEL Core","Pentium"])
print(processor)

## To find the length of a set

print(len(processor))

## To delete a particular value in the set

processor.discard("INTEL Core")
print(processor)

## to remove last element in the set

processor.pop()
print(processor)

## to find the difference between two list

set1 = {"Ajay","Karthick","Krishna"}
set2 = {"Krishna","Karthick","Ritika"}

difference = set2.difference(set1)
print(difference)

## To display the unique items from both the sets

set2.difference_update(set1)
print(set2)

## Intersection 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)

print(z)

## Intersection update

x.intersection_update(y)
print(x)

## IS-DISJOINT

z = x.isdisjoint(y)
print(z)

## IS-SUBSET

z = x.issubset(y)
print(x)

## IS-SYMMETRIC DIFFERENCE

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)

print(z)

## IS-SYMMETRIC DIFFERENCE UPDTAE

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

## UNION OF TWO SET INTO OTHER

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result) 

## TO FIND A VALUE IN A SET

Names = {"ajay","krishnan","karthick","babu","nimmi","ravi","ritika","python"}
search = input("ENter the name you want to search: ")
print(search in Names)

 