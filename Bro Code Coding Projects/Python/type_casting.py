# Typecasting = The process of converting one 
#               data type to another data type.
#               (integers, floats, strings, etc.)
#               Explicit and Implicit Typecasting

name = "Alex Baker" # String
age = 22 # Integer
gpa = 4.1 # Float
student = True # Boolean

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Explicit Typecasting
age = float(age) # Converting Integer to Float
print(age)
print(type(age))

gpa = int(gpa) # Converting Float to Integer
print(gpa) # Drops the decimal value
print(type(gpa))

student = str(student) # Converting Boolean to String
print(student)
print(type(student))

age = bool(age) # Converting Float to Boolean
print(age) # Any non-zero number converts to True
print(type(age))

# Implicit Typecasting
x = 5 # Integer
y = 2.0 # Float

x = x + y # Implicitly converts Integer to Float
print(x)