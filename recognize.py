num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45:   # if else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # if else
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # while loop
    print(x)
    x += 1

pizza_toppings.pop() #pop
pizza_toppings.pop(1)

print(person) # console.log
person.pop('eye_color')
print(person)

for topping in pizza_toppings:  # loop with conditionals
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():  # function 
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # function with parameters
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function with paramaters and default values
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

print(num3)
num3 = 72
fruit[0] = 'cranberry'
print(person['favorite_team']) # print from dictionary
print(pizza_toppings[7])  # print from array
print(boolean)
fruit.append('raspberry') # like push
fruit.pop(1)