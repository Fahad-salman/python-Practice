# you can use path for specific ..\fileName\file.txt
# How to reed file in python ?
my_file = open('README.md')
print(my_file)
print(my_file.read())
print(my_file.readlines())
print(my_file.readline())

# after you done from file you have to close the file
my_file.close()
# just like this or you can use
with open('README.md') as my_file:
    print(my_file.read())
# also you can write 
with open('README.md',mode='a') as my_file:
    text = my_file.write('Hello world! ')
# what if file dose not exist ?
try:
    with open('README.fmd',mode='r') as file_m:
        print(file_m.read())     
except FileNotFoundError as err:
    print('File dose not exist .')
    # raise err   