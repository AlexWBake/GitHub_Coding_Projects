# method = a function that is associated with an object
# in this case we are talking about string methods

name = input('Enter your full name:\n')

print(len(name))  # len is a function that returns the length of the string
                  # length includes spaces

print(name.find(' '))  # find will return the location of the first occurrence of the substring
                       # if the substring is not found, it returns -1
                       # first case is located at 4 when input ('Alex Baker') starts with 0

print(name.rfind(' '))  # rfind will return the location of the last occurrence of the substring

print(name.capitalize())  # capitalize will return the string with the first letter capitalized
print(name.upper())  # upper will return the string in all uppercase letters
print(name.lower())  # lower will return the string in all lowercase letters

print(name.isdigit()) # isdigit will return True if all characters in the string are digits
print(name.isalpha()) # isalpha will return True if all characters in the string are letters
                      # for ('Alex Baker') isalpha will return False because of the space
print(name.isalnum()) # isalnum will return True if all characters in the string are letters or digits

print(name.count('a'))  # count will return the number of occurrences of the substring in the string

print(name.replace(' ', '_')) # replace will replace all examples of a string with your new string

#Project:  build a program where username is no more than 12 characeters, no spaces, and no digits

username = input('Enter your username\n')

if len(username) > 13:
    print('Username can only contain 12 characters')
elif not username.find(' ') == -1:
    print('Username can\'t contain spaces')
elif not username.isalpha():
    print('Username can\'t contain digits')
else:
    print(f'Welcome {username}!!')
    