# Exercise 8 questions => (Create Countdown and hierarchy)

def rectangle(val):
    while True:
        if val == 0:
            break
        else:
            print('')
            val -= 1
            for i in range(val):
                print(i,end='')
            continue
my_value = int(input('Enter any number : '))
rectangle(my_value)