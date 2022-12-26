# if we don't have Atribute or variable 
# we don't want to use init method
class User(object):
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')
# how to let wizard and archer have access to singn_in
# we will use inheritance, pass the pernt class in between the brackets
class Wizard(User): 
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    def attack(self):
        print(f'{self.name} attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows
    def attack(self):
        print(f'{self.name} will attacking with arrows : arrows left - ({self.arrows})')


wizard1 = Wizard('john','Sord','john@gmail.com')
archer1 = Archer('elena',35)


# print(dir(wizard1))
wizard1.attack()
archer1.attack()
print(isinstance(wizard1,Archer),'<< is sup clss ?')
print(isinstance(wizard1,User),'<< is sup clss ?')
print(wizard1.attack())
print(wizard1.sign_in())


