# Exercise 3 questions => 
# (
# chek if magician and expert : "You are a master magician"
# chek if magician but not expert : "at least You're getting there"
# chek if You're not a magician: "You need magic powers"
# )  exercise two

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

print(is_magician, is_expert)

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