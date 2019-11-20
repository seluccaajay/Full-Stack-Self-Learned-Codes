

## creating a stack using a class

class stack:
 def push(self,item):
  self.__items.append(item)
 def pop(self):
  return self.__items.pop()
 def __init__(self):
  self.__items=[]
s1 = stack()
s1.push(10)
s1.push(20)
s1.pop()
s2 = stack()
s2.push(10)
print(s1._stack__items)

