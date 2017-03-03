# Import modules and use sys to exit

import random
import sys

while True:
    print('Your random number is ' + str(random.randint(1, 100)))
    print('Would you like to exit?')
    response = input()
    if response == 'exit':
        print('You typed exit. Backing away slowly...')
        sys.exit()
    print('You typed: ' + response)