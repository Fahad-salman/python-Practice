#  This function will colculate any number colculater

def plus(one,tow):
    return (one+tow)

def minus(one,tow):
    return (one-tow)

def multiply(one,tow):
    return (one*tow)

def divide(one,tow):
    return (one/tow)

def culculate():
    # name = input('Enter your name please : ')
    # print('welcome ',name,' i like your n610ame')
    while True:
        try:
            numberOne = float(input('enter the first number: '))
        except ValueError:
            print("Enter number only")
            continue
        else:
            break
    while True:
        try:
            numberTwo = float(input('enter the second number: '))
        except ValueError:
            print('enter number only')
        else:
            break
    typeOperation = input('enter the type of operation: ')
    if(typeOperation == '+' ):
        print(numberOne, typeOperation ,numberTwo,' = ',plus(numberOne,numberTwo))
    elif typeOperation == '-':
        print(numberOne, typeOperation ,numberTwo,' = ',minus(numberOne,numberTwo))
    elif typeOperation == '*' :
        print(numberOne, typeOperation ,numberTwo,' = ', multiply(numberOne,numberTwo))
    elif typeOperation == '/' :        
        print(numberOne, typeOperation ,numberTwo,' = ',divide(numberOne,numberTwo))
    else:
        print("error: unknown type => try use one of them ( + , - , * , / )")

while True:
    res = input('stop or complete ? ')
    if res == 'stop':
        break
    else:
        while True:
            try:
                culculate()
            except ValueError:
                print("Error calculating")
            except ZeroDivisionError:
                print("you can't Division by Zero ! ")
            else:
                break