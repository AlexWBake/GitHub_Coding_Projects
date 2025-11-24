
unit = input('Is this in Celsius or Farenheit? (C/F):\n')

if unit == 'C' or unit == 'c':
    temp = float(input("Enter temperature in Celsius:\n"))
    fahrenheit = (temp * 1.8) + 32
    print(f'Temperature in Fahrenheit: {fahrenheit}°F')

elif unit == 'F' or unit == 'f':
    temp = float(input('Enter temperature in Farenheit:\n'))
    celsius = (temp - 32) / 1.8
    print(f'Temperature in Celsius: {celsius}°C')
    
else: 
    print('Invalid input. Please enter C for Celsius or F for Farenheit.')


    