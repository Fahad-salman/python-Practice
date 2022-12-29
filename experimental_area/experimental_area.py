# side effects 
# pure function


class Status():
    def __init__(self,bool):
        self.bool = bool
    def sign_in(bool):
        player_conation = bool
        if player_conation:
            return'player online ...'
        else:
            return 'player offline ...'

class Attacker(Status):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def info(self):
        return self.name , self.power

# class Deffender(status):
#     pass

player = Attacker(name='Hanzo',power='Bow')
# print(list(player.info()))
print(player.info())
print(player.sign_in())
# print(player.sign_in(True))