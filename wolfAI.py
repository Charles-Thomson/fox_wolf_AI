from tkinter import *
from typing import Collection
from AI import AISupportingMethods
from NewSetUp import build_canvas
from foxAI import DetermineGoodAndBadMoves
import collections


def MainWolfAI(wolfs: list, foxs: list, built_canvas: Canvas, node_size: int) -> None:
    """Main wolf loop"""
    
    for wolf in wolfs:
        SetAnimalsInRange(wolf, foxs)
        SetAnimalNextMove(wolf,wolfs)
        SetAnimalMovingTo(wolf)
        print(wolf)
        
    MoveWolf(wolfs,built_canvas,node_size)
     
def SetAnimalsInRange(wolf: object, foxs: list) -> None:
    """Find & set the animals in range of the wolf"""
    wolf.animals_in_range = AISupportingMethods.DetectAnimalsInRange(wolf, foxs)
    
def SetAnimalNextMove(wolf: object,wolfs: list) -> None:
    """Find & set the next move of the wolf"""
    wolf.animal_next_move = FindNextMove(wolf,wolfs)

def SetAnimalMovingTo(wolf:object) -> None:
    
    """Declare where the animal is moving to next (x,y) - for collision purpaces"""

    current_x, current_y = wolf.animal_location
    move_x_by, move_y_by = wolf.animal_next_move
    moving_to_x = current_x + move_x_by
    moveing_to_y = current_y + move_y_by
    wolf.animal_moving_to = (moving_to_x,moveing_to_y)


def FindNextMove(wolf: object,wolfs: list) -> tuple:
    return FindBestMove(DeterminePossibleMoves(wolf, wolf.animals_in_range),wolf,wolfs)

def DeterminePossibleMoves(wolf: object, other_animal_coords: list) -> tuple: 
    """Find all the possible 'good' moves based on the locations of animals around the wolf"""

    possible_moves = []
    wolf_coords_x, wolf_coords_y = wolf.animal_location
    
    for other_animals_coord_x, other_animals_coord_y in other_animal_coords:
        # +x +y
        if wolf_coords_x >= other_animals_coord_x and wolf_coords_y >= other_animals_coord_y:
            possible_moves.append(((-1,-1)))
            possible_moves.append((0,-1))
            possible_moves.append((-1,0))
        # -x +y
        if wolf_coords_x <= other_animals_coord_x and wolf_coords_y >= other_animals_coord_y:
            possible_moves.append((1,-1))
            possible_moves.append((0,-1))
            possible_moves.append((1,0))
        # +y -x 
        if wolf_coords_x >= other_animals_coord_x and wolf_coords_y <= other_animals_coord_y:
            possible_moves.append((-1,1))
            possible_moves.append((0,1))
            possible_moves.append((-1,0))
        # -y -x 
        if wolf_coords_x <= other_animals_coord_x and wolf_coords_y <= other_animals_coord_y:
            possible_moves.append((1,1))
            possible_moves.append((0,1))
            possible_moves.append((1,0))
    
    return possible_moves
        

# issue in here - check for collision, will need to pass all the defined moves as the new location or cange to assign move -> move over assign all -> move all 
def FindBestMove(possible_moves: list[tuple],wolf: object ,wolfs: list) -> tuple:
    """Find the most common 'good' move from the possible moves - if none then return no move (0,0)"""
    print("Find best called", wolf.animal_ID)

    if possible_moves:
        possible_best_move = collections.Counter(possible_moves).most_common(1)[0][0]
        if CheckMoveForPossibleCollision(possible_best_move,wolf,wolfs) == True:
            return possible_best_move
        
    return (0,0)
    # No move  


def CheckMoveForPossibleCollision(best_move: tuple,wolf: object, wolfs: list) -> bool:
    """Checking for collision with other wolfs currently - based on moving to by adding current to possible next move"""

    best_x, best_y = best_move
    this_wolf_ID = wolf.animal_ID
    current_wolf_x, current_wolf_y = wolf.animal_location
    possible_new_x = current_wolf_x + best_x
    possible_new_y = current_wolf_y + best_y
    this_possible_new_wolf_location = (possible_new_x,possible_new_y)
    
    # Ceck to see if it will colide with any other wolf moves 
    for wolf in wolfs:
        if wolf.animal_moving_to == this_possible_new_wolf_location and wolf.animal_ID != this_wolf_ID:
            return False
        else:
            return True


def MoveWolf(wolfs: list[object],built_canvas: Canvas,  node_size: int) -> None:
    """Moving all wolfs to new best"""
    
    for wolf in wolfs:
        next_move_x, next_move_y = wolf.animal_next_move
        next_move_x_long_coord, next_move_y_long_coord,x2,y2 = AISupportingMethods.ConvertToLongCoords(next_move_x, next_move_y, node_size)
        built_canvas.move(wolf.animal_ID,next_move_x_long_coord, next_move_y_long_coord)
        UpdateWolfData(wolf, built_canvas)

def UpdateWolfData(wolf: object, built_canvas: Canvas) -> None:
    """Update the Wolf locations for each wolf - Clear the next move & animals in Range"""

    old_wolf_x, old_wolf_y = wolf.animal_location
    moved_wolf_x_by, moved_wolf_y_by = wolf.animal_next_move

    wolf.animal_location = (old_wolf_x + moved_wolf_x_by,old_wolf_y + moved_wolf_y_by)
    wolf.animal_next_move = []
    wolf.animals_in_range = []
    wolf.animal_moving_to = ()

