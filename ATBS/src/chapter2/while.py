# Annoying while loop

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# Annoying infinite while loop with break
# break with instantly break out of the loop and execute the next line

while True:  # (1)
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# Annoying infinite while loop with continue
# continue will jump to the start of the loop and reevaluate the loop condition

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
