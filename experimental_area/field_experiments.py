while True:
    res = input('ok let\'s begin , chose one of them , ( Play , Password , Colculate_Age , Close ) : ')
    if res == 'Close':
        break
    elif res == 'Password':
        userName = input('Enter your name: ')
        passWord = input('Enter your password: ')
        lengthPassword = len(passWord)
        hidePassword = ('*' * lengthPassword)
        print(f'welcome {userName} , Your password {hidePassword} is {lengthPassword} letters long .')
    elif res == 'Colculate_Age':
        print('will let\'s do it ')
        currentYear = 2022
        while True:
            try:
                birthYear = float(input('What year were you born ? '))
            except ValueError:
                    print('Use number please')   
            else:
                break
        age = currentYear-birthYear
        print(f'Your age is {age} years old')
    elif res == 'Play':
        list_yes = [
            'Yes',
            'YEs',
            'YES',
            'yES',
            'yeS',
            'yes',
            'Y',
            'y',
        ]

        list_no = [
            'N',
            'n',
            'No',
            'NO',
            'nO',
            'no',
        ]

        is_magician = input('(Yes or No) Do you have magic skills ? ')
        is_expert = input('(Yes or No) Are you expert ? ')

        # print(is_magician, is_expert)

        if is_magician in list_yes and is_expert in list_yes:
            print('You are a master magician')
        elif is_magician in list_yes and is_expert in list_no:
            print('at least You\'re getting there')
        elif is_magician in list_no and is_expert in list_yes:
            print('at least You\'re getting there')
        elif is_magician in list_no and is_expert in list_no:
            print('You need magic powers')
        else:
            print('error: unknown error')