import abc
from enum import Enum
from AI import AISupportingMethods


def BasicMovmentAlgorithm(self: object) -> None:
    print("In the alg")
    good_moves = []
    bad_moves = []
    fox_coord_X, fox_coord_Y = self.animal_move_data.animal_location

    for coord_X, coord_Y in self.animal_move_data.animals_in_range:
        # +x
        if coord_X > fox_coord_X and coord_Y == fox_coord_Y:
            bad_moves.extend([(1,0),(1,1),(1,-1)])
            good_moves.extend([(-1,0),(-1,-1),(-1,1)])
            
        # -x
        if coord_X < fox_coord_X and coord_Y == fox_coord_Y:
            bad_moves.extend([(-1,0),(-1,-1),(-1,1)])
            good_moves.extend([(1,0),(1,-1),(1,1)])
            
        # +y
        if coord_X == fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(0,1),(1,1),(-1,1)])
            good_moves.extend([(0,-1),(1,-1),(-1,-1)])
            
        # -y
        if coord_X == fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(0,-1),(-1,-1),(1,-1)])
            good_moves.extend([(0,1),(-1,1),(1,1)])
            
        # +x +y
        if coord_X > fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(1,0),(0,1),(1,1)]) 
            good_moves.extend([(-1,-1),(-1,0),(0,-1)])
            
        # -x -y
        if coord_X < fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(-1,0),(0,-1),(-1,-1)])
            
            good_moves.extend([(1,1),(1,0),(0,1)])
            
        # +x -y
        if coord_X > fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(0,-1),(1,0),(1,-1)]) 
            good_moves.extend([(-1,1),(-1,0),(0,1)])
            
        # -x +y
        if coord_X < fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(-1,0),(0,1),(-1,1)])
            good_moves.extend([(1,-1),(1,0),(0,-1)])
            
    good_moves = [move for move in good_moves if move not in bad_moves]
    self.animal_move_data.animal_next_move = AISupportingMethods.RebuildDetermineBestMove(good_moves)







class FoxMovementAlgoritm(Enum):
    """Enumerate the Movment Algorithms"""
    
    BASIC = BasicMovmentAlgorithm
    