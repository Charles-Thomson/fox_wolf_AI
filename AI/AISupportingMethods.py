import collections

def DetectAnimalsInRange(main_animal: object, other_animals: list[object]) -> list:
    """Detect animals in range of the given animal, returns list of animals in range coords (x,y) """

    main_animal_coord_X, main_animal_coord_Y = main_animal.animal_move_data.animal_location
    animals_in_range = []

    for other_animal in other_animals:
        other_animal_coord_X, other_animal_coord_Y = other_animal.animal_move_data.animal_location

        if main_animal_coord_X in range(int(other_animal_coord_X - main_animal.animal_core_data.animal_sight_range),int(other_animal_coord_X + main_animal.animal_core_data.animal_sight_range)) and main_animal_coord_Y in range(int(other_animal_coord_Y - main_animal.animal_core_data.animal_sight_range), int(other_animal_coord_Y + main_animal.animal_core_data.animal_sight_range)):
            animals_in_range.append(other_animal.animal_move_data.animal_location)
    
    return animals_in_range

def SetAnimalMovingTo(animal: object) -> None:
    """Set the animal data for moving to"""
    

    current_location = animal.animal_move_data.animal_location
    move_by = animal.animal_move_data.animal_next_move

    new_coords = tuple(sum(x) for x in zip(current_location,move_by))
    animal.animal_move_data.animal_moving_to = new_coords



def AnimalWouldMoveTo(animal_current_location: tuple, animal_potential_move: tuple):
    """Helper function used in DeterminBestMove"""
    
    return tuple(sum(x) for x in zip(animal_current_location,animal_potential_move))


# Need to pass the position the animal will move to in here 
def RebuildDetermineBestMove(animal_current_location: tuple, good_moves: list[tuple], collision_detection: object ) -> tuple:
    """Finding the optimal move that is also allowed"""

    while True:
        if good_moves == []:
            return (0,0)
        potential_move = collections.Counter(good_moves).most_common()[0][0]
        potential_new_location = AnimalWouldMoveTo(animal_current_location,potential_move)
        
        if collision_detection.CollisionChecking(potential_new_location) == True:
            return potential_move
        else:
            good_moves = [move for move in good_moves if move != potential_move]
            

        
def MoveAnimal(animal: object, canvas_data: object) -> None:
    """Move the animal to new postion - move made by an ammount based on current position """

    animal_moving_to_X , animal_moving_to_Y = animal.animal_move_data.animal_next_move
    move_X_by , move_Y_by,x2,y2 = ConvertToLongCoords(animal_moving_to_X , animal_moving_to_Y, canvas_data.node_size)
    canvas_data.canvas.move(animal.animal_core_data.animal_ID,move_X_by , move_Y_by )

def UpdateAnimalData(animal:object) -> None:
    animal.animal_move_data.animal_location = animal.animal_move_data.animal_moving_to
    animal.animal_move_data.animal_moving_to = ()
    animal.animal_move_data.animal_next_move = ()
    animal.animal_move_data.animals_in_range = []

    pass 

def ConvertToShortCoords(animal,built_canvas, node_size) -> tuple:
    """Convert the long coordinates used by tkinter to x,y  """

    x1,y1,x2,y2 = built_canvas.coords(animal)
    x = (x1 / node_size)
    y = (y1 / node_size)

    return (x,y) 

def ConvertToLongCoords(animal_x, animal_y, node_size) -> int:
    """Convert the short x,y coordinates back to the long coordinates """
    
    x1 = (animal_x * node_size)
    y1 = (animal_y * node_size)
    x2 = x1 + node_size
    y2 = y1 + node_size

    return x1,y1,x2,y2
