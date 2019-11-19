processor = {"name":"I5","model":"7th Gen","Brand":"Intel","Price":"25000"}
processor["Price"] = 45000
print(processor)

## TO PRINT ONLY THE KEYS OF DICT

for x in processor:
 print(x)
 
## Remove all the elements from the dict using clear()

Processor = {
  "brand": "Intel",
  "model": "I5",
  "year": 2016
}

Processor.clear()

print(Processor)

## To copy a particular Dict using a dict function

Bike = {
  "brand": "Honda",
  "model": "Dio BS4",
  "year": 2017
}

x = Bike.copy()

print(x)

## Creating a dict from two variables of tuples using a fromkeys() function

x = ('Ajay','Ritika','Senba')
y = 0

family = dict.fromkeys(x,y)
print(family)

## To get the value assigned in a particular key in a dict

Bike = {
  "brand": "Honda",
  "model": "Dio BS4",
  "year": 2017
}

x = Bike.get("model")
 
print(x)

## We can write the dict key value pairs by using the items() function

Bike = {
  "brand": "Honda",
  "model": "Dio BS4",
  "year": 2017
}

x = Bike.items()

print(x)

## To print the keys alone we can use the keys function

car = {
  "brand": "Volkswagen",
  "model": "Polo",
  "year": 2016
}

x = car.keys()

print(x) 

## We can use pop function to delete the particular itm in the dict

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car) 

## To blindly remove the last item from the dict

bike = {
  "brand": "Hero",
  "model": "Splendor",
  "year": 2003
}

bike.popitem()

print(bike) 

## We can change the value of a key and make it as a default valuse using the setdefault funtion

processors = {
  "brand": "Intel",
  "model": "I5",
  "year": 2016
}

x = processors.setdefault("model", "I7")

print(x) 

## Similar to add function we have a function called update() funtion to change value of a key in a dict

processors = {
  "brand": "Intel",
  "model": "I5",
  "year": 2016
}

processors.update({"model": "I7"})

print(processors)

## Need to see only the values and not the keys? use the values() function.

processors = {
  "brand": "Intel",
  "model": "I5",
  "year": 2016
}

x= processors.values()
print(x)