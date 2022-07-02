# from re import U
from tkinter import *
import tkinter as tk
from AI import AISupportingMethods
import collections 

def MainFoxAI(foxs: list,wolfs: list ,built_canvas: Canvas,node_size: int) -> None:
    """Main process for the AI - Sets the animals in range, next move and then calls for the movement """

    for fox in foxs:
        SetAnimalsInRange(fox,wolfs)
        fox.animal_next_move = FindNextMove(fox)
    MoveFoxs(foxs,built_canvas,node_size)


def SetAnimalsInRange(fox: object,wolfs: list) -> None:
    fox.animals_in_range = AISupportingMethods.DetectAnimalsInRange(fox,wolfs)

def SetAnimalNextMove(fox: object) -> None:
    fox.animal_next_move = FindNextMove(fox)

def FindNextMove(fox: object ) -> tuple:
    return DetermineBestMove(DetermineGoodAndBadMoves(fox,fox.animals_in_range))


def DetermineGoodAndBadMoves(fox: object,other_animal_coords: list) -> list[tuple]:
    """Takes in the fox object and the coordinates of other animals in range, determians move based  on other animals x,y locations"""

    unusable_moves = set()
    good_move = []
    fox_coord_X, fox_coord_Y = fox.animal_location
    for coords in other_animal_coords:
        other_animal_coord_X,other_animal_coord_Y = coords

        # +x +y
        if other_animal_coord_X >= fox_coord_X and other_animal_coord_Y >= fox_coord_Y:
            unusable_moves.add((1,0)) 
            unusable_moves.add((0,1))
            unusable_moves.add((1,1))
            good_move.append((-1,-1))
            good_move.append((-1,0))
            good_move.append((0,-1))
        # -x -y
        if other_animal_coord_X <= fox_coord_X and other_animal_coord_Y <= fox_coord_Y:
            unusable_moves.add((-1,0))
            unusable_moves.add((0,-1))
            unusable_moves.add((-1,-1))
            good_move.append((1,1))
            good_move.append((1,0))
            good_move.append((0,1))
        # +x -y
        if other_animal_coord_X >= fox_coord_X and other_animal_coord_Y <= fox_coord_Y:
            unusable_moves.add((0,-1)) 
            unusable_moves.add((1,0))
            unusable_moves.add((1,-1))
            good_move.append((-1,1))
            good_move.append((-1,0))
            good_move.append((0,1))
        # -x +y
        if other_animal_coord_X <= fox_coord_X and other_animal_coord_Y >= fox_coord_Y:
            unusable_moves.add((-1,0))
            unusable_moves.add((0,1))
            unusable_moves.add((-1,1))
            good_move.append((1,-1))
            good_move.append((1,0))
            good_move.append((0,-1))

    return good_move, unusable_moves

def DetermineBestMove(Good_and_bad_moves) -> tuple:
    """Finds 'best' move based on the most common 'good' move - if no most common use the first given 'good' move - else make no move"""

    good_moves, bad_moves = Good_and_bad_moves
    possible_best_moves = [move for move in good_moves if move not in list(bad_moves)]

    if possible_best_moves:
        return collections.Counter(possible_best_moves).most_common(1)[0][0] # give most common or first in good list 
    else:
        return(0,0) # no move
    

def MoveFoxs(foxs: list,built_canvas: Canvas,node_size: int) -> None:
    """Makes the 'best' move as set by DetermineBestMove for each fox"""

    for fox in foxs:
        short_coord_x, short_coord_y = fox.animal_next_move
        long_coord_x, long_coord_y, x2,y2 = AISupportingMethods.ConvertToLongCoords(short_coord_x, short_coord_y,node_size)
        built_canvas.move(fox.animal_ID,long_coord_x,long_coord_y)  # tkinter move done based on ID
        UpdateFoxData(fox)

def UpdateFoxData(fox: object) -> None: 
    """Update the fox location data using the current next move and current location - clear animal next move and animals in range"""

    fox_x, fox_y = fox.animal_location
    move_x_by, move_y_by = fox.animal_next_move

    fox.animal_location = ((fox_x + move_x_by),(fox_y + move_y_by))
    fox.animal_next_move = ()
    fox.animals_in_range = []
    
    


    