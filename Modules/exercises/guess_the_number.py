# exercises create simple game -> Guess the number between 1 and 10

import random

def guess_number(answer):
    guesser = random.randint(1,10)
    if guesser == answer:
        print('Woow!! You got the number !!')
    else:
        print(f'ops {answer} wrong answer , the correct answer is {guesser}')
        

while True:
    try:
        value = int(input('Guess the number between 1 and 10 ? '))
    except ValueError: 
        print('Please use a number between 1 and 10')
    else:
        guess_number(value)
        break

