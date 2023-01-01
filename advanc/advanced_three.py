# Decorators
# Decorators super charge are function
# Hight Order Function HOC

# example 1

def greet_Decorator(func):
    def wrap_func(msg):
        print('********')
        func(msg)
        print('********')
    return wrap_func

# greet(greeting)
@greet_Decorator
def greeting(msg):
    print(msg)

greeting('Hello I\'m Fahad')

# example 2

def my_decorator(func):
    def warp_function(*args, **kwargs):
        func(*args, **kwargs)
    return warp_function

@my_decorator
def my_function(simple_msg,name):
    print(f'You have to know {name}, {simple_msg}')

my_function('Your time is your treasure',name='Fahad')