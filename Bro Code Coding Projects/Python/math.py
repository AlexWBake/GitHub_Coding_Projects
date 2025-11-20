# Arithmatic operations
import math

friends = 9
friends = friends + 1 # increase friends by 1
print(friends)
friends += 1 # shorthand for friends = friends + 1 (Augmented assignment)
print(friends)
friends = friends - 2 # decrease friends by 2
print(friends)
friends -= 2 # shorthand for friends = friends - 2 (Augmented assignment)
print(friends)
friends *= 2 # double the number of friends
print(friends)
friends /= 2 # halve the number of friends
print(friends)
remainder = 10 % 3 # modulus operator gives the remainder 10 / 3 = 3 with remainder of 1
print(remainder)

x = 3.14
y = -4
z = 5

print(round(x)) # rounds to nearest integer
print(round(x, 1)) # rounds to 1 decimal place
print(abs(y)) # absolute value (distance away from zero(makes number positive))
print(pow(2, 3)) # raises 2 to the power of 3 (2^3)
print(max(x,y,z)) # returns the maximum value
print(min(x,y,z)) # returns the minimum value
print(math.pi) # prints value of pi from math module
print(math.e) # prints value of e from math module
print(math.sqrt(4)) # prints the square root of 4
print(math.ceil(3.1)) # rounds to the next highest integer
print(math.floor(3.9)) # rounds to the next lowest integer

# Calculate the circumference and area of a circle
radius = int(input("What is the radius of your circle\n"))
circumference = 2 * math.pi * radius
print(f'The circumference of your circle is {circumference}')
area = math.pi * pow(radius, 2)
print(f'The area of your circle is {area}')

# Find the length of the hypotenuse of a right angled triangle
a = int(input("Enter side a\n")) 
b = int(input("Enter side b\n"))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'The length of the hypotenuse is {c}')