# Quick program to demonstrate use of the round() builtin function

print('Please enter a floating point number')
inputFloat = input()
print('How many decimal places would you like to round off to?')
decimalPlaces = input()
print('Your number is rounded off to ' + str(round(float(inputFloat), int(decimalPlaces))))
