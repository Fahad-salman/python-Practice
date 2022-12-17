# Dictionary (dict) like map in other languages
# Dictionary is unordered key value
# The key in dictionary have to be a unique 
dictionary = {
    'a':1,
    'b':2,
    'c':3,
}

print(dictionary['a']) # will print value from the key
# to avoid error use dict.get('key name' , 'value (get will take this value when key is None)')

print(dictionary.get('age','it is None'))

# lets use dict on variable

user = dict(name='Fahad')
print(user.get('name','it is None'))

# we can use (in) in the dictionary

print('a' in dictionary) # if not found its False , if found it will return True
#  you can use chake the key and value from dictionary by using
#  dict.key() method 
#  dict.value() method 
#  dict.items() method for both keys and values
print(dictionary.items())

# remove method in dictionary
# pop() method
# popitem() method
# clear() method

# You can also update the dictionary key by using dict.update({'key':'value'})
# it will update the key , what will happen when key does not exist ? it will create a new key and value 
print(dictionary.update({'key':'value'}))
print(dictionary)