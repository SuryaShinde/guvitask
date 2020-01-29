import random

strs = ['dad', 'mom', 'bat', 'car', 'bus', 'pen', 'dog', 'cat']
points = 0
string = random.choice(strs)

for i in range(5):
    c = input('Enter a character: ')
    if c in string  and c!='':
        print('Good')
        points = points + 1
        if points == 3:
            break
    else:
        print('You entered a wrong character')
        
if points == 3:
    print('Won')
else:
    print('Lost')
