from enum import Enum
from AI import AISupportingMethods

def BasicMovmentAlgorithm(self: object) -> None:
    good_moves = []
    wolf_coord_X, wolf_coord_Y = self.animal_move_data.animal_location

    for coord_X, coord_Y in self.animal_move_data.animals_in_range:
        # +x +y
        if wolf_coord_X >= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(-1,-1),(0,-1),(-1,0)])
            
        # -x +y
        if wolf_coord_X <= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(1,-1),(0,-1),(1,0)])
            
        # +y -x 
        if wolf_coord_X >= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(-1,1),(0,1),(-1,0)])
            
        # -y -x 
        if wolf_coord_X <= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(1,1),(0,1),(1,0)])
            

    self.animal_move_data.animal_next_move = AISupportingMethods.RebuildDetermineBestMove(good_moves) # call to method in AI support


class WolfMovementAlgorithm(Enum):
    BASIC = BasicMovmentAlgorithm
    
