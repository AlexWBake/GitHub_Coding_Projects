# if = Do some code only IF some condition is True
#      Else do something else

age = int(input('Enter your age:\n'))

if age >= 150: # Order of conditions matters!
    print('You dead!') # 150 must be first to catch unrealistic ages
elif age < 0:
    print('You haven\'t been born yet!\n')
elif age >= 18:
    print('You are now signed up!\n')
else:
    print('You must be at least 18 to sign up.\n')

# Exercise 1
response = input('Would you like food? (Y/N)\n') # = Assignment operator

if response == 'Y' or response == 'y': # == must be used for comparison
    print('Have some food!\n')
elif response == 'N' or response == 'n':
    print('No food for you!\n')
    
# Exercise 2
name = input('Enter you name.\n')

if name == '':
    print('You did not enter a name!\n')
else:
    print(f'Hello, {name}!\n')

# Exercise 3
for_sale = True

if for_sale: # Same as if for_sale == True:
    print('This item is for sale!\n')
else:
    print('This item is not for sale!\n')