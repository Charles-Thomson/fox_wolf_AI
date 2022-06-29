from re import U
from tkinter import *
import tkinter as tk
from AI import AISupportingMethods
from AI import moves
import collections 


def DetectWolfsInRange(foxs,wolfs) -> None:
    for fox in foxs:
        fox.animals_in_range = AISupportingMethods.DetectAnimalsInRange(fox,wolfs)
    FindNextMove(foxs)

def FindNextMove(foxs) -> None:
    for fox in foxs:
        other_animal_coords = [animal.animal_location for animal in fox.animals_in_range]
        good_moves, bad_moves = DetermineGoodAndBadMoves(fox,other_animal_coords)
        best_move = DetermineBestMove(good_moves, bad_moves)
        print("best move ", best_move)


def DetermineGoodAndBadMoves(fox,other_animal_coords) -> list:
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

def DetermineBestMove(good_moves, bad_moves) -> tuple:
    possible_best_moves = [move for move in good_moves if move not in list(bad_moves)]
    # give most common or first in good list 
    return collections.Counter(possible_best_moves).most_common(1)[0][0]
    
   
    