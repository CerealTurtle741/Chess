class piece:
   def __init__(self, type, value, movement):
     self.type= type
     self.value= value
     self.movement= movement
pawn= piece('pawn', 1, 'forward 1')
print(pawn)
