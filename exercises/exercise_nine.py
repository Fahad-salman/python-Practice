# Exercise 9 questions => (check if the value in the list or not then return the index of the value you want) 


my_list = ['Fahad','Sultan','Salman','Saleh','Saad','Khaled','Ali']
search = input('waht are you looking for ? ')

def find_item(val):
    if val not in my_list:
        print(f'{val} Not found.')
    else:
        print(f'This is the index for ({val}) ',my_list.index(val))

find_item(search)