# Implement a class to hold room information. This should have name and
# description attributes.

#class = noun
#attributes = adjectives 
#self = this 
#self refers to the instance of the class
#repr provides more info for devs 

class Room:
    """This Room has information"""  
    def __init__(self, name, description=[],):
        self.name = name 
        self.description = description

    def __str__(self):
        return 'I am in a state of despair'

    def __repr__(self):
        return f'Room({self.name}, {self.description})'

    


adventure_room = Room('Room Of Despair', description=['ghosts', 'crying', 'darkness', 'defeat'])
print(repr(adventure_room)) 
print(str(adventure_room))