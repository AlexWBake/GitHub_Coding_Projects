name = input("What is your name?\n") # \n means new line
age = int(input("How old are you?\n")) # inputs are string by default, so we convert to int
age = age + 2

print(f'Hello, {name}! Welcome to my code')
print(f'You are {age} years old!')

# Mad Libs project
adjective1 = input("Enter an adjective:\n")
noun = input("Enter a noun:\n")
adjective2 = input("Enter another adjective:\n")
verb = input("Enter a verb:\n")

print(f'Today I went to a {adjective1} zoo')
print(f'In an exhibit, I saw {noun}')
print(f'{noun} was {adjective2} and {verb}ing all over the place!')

# Finding the area of Rectangle
length = float(input("Enter the length of the rectangle:\n"))
width = float(input("Enter the width of the rectangle:\n"))

area = length * width
print(f'The area of the rectangle is {area}')

# Shopping List
item = input("What item would you like to buy?\n")
price = float(input("What is the price?\n"))
quantity = int(input("How many of this item do you want?\n"))

total_cost = price * quantity
print(f'You have bought {quantity} {item}(s) for a total of ${total_cost}')