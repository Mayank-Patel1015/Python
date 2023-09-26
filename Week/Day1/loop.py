# basic
for i in range(150):
  print(i+1)

# by 5
for i in range(30):
  print((i+1)*5)

# Coding Dojo counting
for i in range(100):
  if (i+1)%10 == 0:
    print("Coding Dojo")
  elif (i+1)%5 == 0:
    print("Coding")
  else:
    print(i+1)

# big sum
big_sum = 0
for i in range(500001):
  big_sum += i
print(big_sum)

for i in range(2018, 0, -4):
  print(i)

def flexibleCounter(lowNum, highNum, mult):
  for i in range( lowNum, highNum+1, 1):
    if i % mult == 0:
      print(i)

flexibleCounter(2,10,2)