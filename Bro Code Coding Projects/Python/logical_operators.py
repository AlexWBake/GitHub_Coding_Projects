# Logical Operators = Only 3 exist in Python, Used to combine conditional statements
#               and = checks if two or more conditions are True
#                or = checks if at least one condition is True
#               not = True if condition is False, and vice versa

a = 25

if a > 0 and a < 30:
    print('A is between 0 and 30')
else:
    print('A is not between 0 and 30')
    

if a == 25 or a == 30:
    print('A is either 25 or 30')
else:
    print('A is not either 25 or 30')
      
if not a == 20:
    print('A is not 20')
