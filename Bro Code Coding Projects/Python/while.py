# while loop =  executes some code WHILE a condition remain true

name = input("Enter your name\n")

while name == '': # will keep prompting them until name is entered
    print('You did not enter your name')
    name = input("Enter you name\n") # If this wasn't here it would be an infinite loop
else:
    print(f'Hello {name}')
    
age = int(input('Enter your age\n'))

while age < 0:
    print('You haven\'t been born yet')
    age = int(input('Enter your age\n'))

print(f'You are {age} years old')
    
food = input("Enter a food you like (q to quit)\n")

while not food == 'q':
    print(f'I like {food}')
    food = input("Enter a food you like (q to quit)\n")

print('bye')