
unit = input('Is this in Celsius, Farenheit, or Kelvin? (C/F/K):\n').upper()

convert = input('Do you want to convert to Celsius, Farenheit, or Kelvin? (C/F/K):\n').upper()

temp = float(input(f'Enter temperature in {unit}\n'))

if unit == 'C':
    if convert == 'F':
        fahrenheit = (temp * 1.8) + 32
        print(f'{temp}°C = {fahrenheit}°F')
    elif convert == 'K':
        kelvin = temp + 273.15
        print(f'{temp}°C = {kelvin}°K')
    elif convert == 'C':
        print(f'{temp}°C = {temp}°C')
        

elif unit == 'F':
    if convert == 'C':
        celsius = (temp - 32) / 1.8
        print(f'{temp}°F = {celsius}°C')
    elif convert == 'K':
        kelvin = (temp - 32) / 1.8 + 273.15
        print(f'{temp}°F = {kelvin}°K')
    elif convert == 'F':
        print(f'{temp}°F = {temp}°F')
        
elif unit == 'K':
    if convert == 'C':
        celsius = temp - 273.15
        print(f'{temp}°K = {celsius}°C')
    elif convert == 'F':
        fahrenheit = (temp - 273.15) * 1.8 + 32
        print(f'{temp}°K = {fahrenheit}°F')
    elif convert == 'K':
        print(f'{temp}°K = {temp}°K')
        
else: 
    print('Invalid input. Please enter C for Celsius or F for Fahrenheit.')


    