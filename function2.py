def countdown(x):
  list = []
  for i in range(x, -1, -1):
    list.append(i)
  return list

print(countdown(100))

def printAndReturn(x, y):
  print(x)
  return y

printAndReturn(1, 2)

def firstPlusLength(list):
  return list[0] + len(list)

print(firstPlusLength([1,2,3,4]))

def values_greater_than_second(list, x):
  newList = []
  for i in range(len(list)+1):
    if i > x: 
      newList.append(i)
  return newList

print(values_greater_than_second([1,2,3,4,5], 3))