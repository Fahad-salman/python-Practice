# you can use path for specific ..\fileName\file.txt
# How to reed file in python ?
my_file = open('file_name.whatever')
print(my_file)
print(my_file.read())
print(my_file.readlines())
print(my_file.readline())

# after you done from file you have to close the file
my_file.close()
# just like this or you can use
with open('file_name.whatever') as my_file:
    print(my_file.read())
# also you can write 
with open('file_name.whatever',mode='a') as my_file:
    text = my_file.write('Hello world! ')