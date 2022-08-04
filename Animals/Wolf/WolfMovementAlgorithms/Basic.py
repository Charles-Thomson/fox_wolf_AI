from Animals.SharedFunctunality import HelperFunctions

def BasicMovementAlgorithm(wolf: object ,collision_detection: object, canvas_data: object) -> None: 
    """Basic process to determin best move for the animal"""

    good_moves = []
    wolf_coord_X, wolf_coord_Y = wolf.animal_move_data.animal_location

    for coord_X, coord_Y in wolf.animal_move_data.animals_in_range:
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

    
    wolf_current_location = (wolf_coord_X, wolf_coord_Y)
    wolf.animal_move_data.animal_next_move = HelperFunctions.RebuildDetermineBestMove(wolf_current_location,good_moves,collision_detection) # Need to work it into here!!
