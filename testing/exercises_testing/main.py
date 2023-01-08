# exercises create simple game -> Guess the number between 1 and 10
# then test the game .
# python -m unittest -v

import random

def guess_number(answer,gass):
    if gass == answer:
        print('Woow!! You got the number !!')
        return True
    else:
        print(f'ops {answer} wrong answer , the correct answer is {gass}')
        return False
        
if __name__ == '__main__':
    guesser = random.randint(1,10)
    # print(guesser)
    while True:
        try:
            value = int(input('Guess the number between 1 and 10 ? '))
        except ValueError: 
            print('Please use a number between 1 and 10')
        else:
            guess_number(value,guesser)
            break

