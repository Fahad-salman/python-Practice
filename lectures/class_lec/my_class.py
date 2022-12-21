# simple example we want to create a game by using class *Chose any idei 
# I chose uncharted game .

class PlayerCharacter:
    memberShip = True # This is a class Opject Atribute , it's static and not dynamic 
    def __init__(self,name,age,gender):
        if (PlayerCharacter.memberShip): # we can use PlayerCharacter.memberShip or use self.memberShip
            self.name = name # Atributes
            self.age = age # Atributes
            self.gender = gender # Atributes only (Male or Female) Nothing else .
            # self.chapterName = chapterName # Atributes 

    
    def playerInfo(self):
        '''
        Info: will return everything about the player Character. 
        '''
        return self.name, self.age, self.gender
    
    
playerNate = PlayerCharacter('Nate',35,'Male')
playerElena = PlayerCharacter('Elena',34,'Female')
playerSam = PlayerCharacter('Sam',41,'Male')

# nate and elena and sam 

print(playerNate.playerInfo())
print(playerElena.playerInfo())
print(playerSam.playerInfo())