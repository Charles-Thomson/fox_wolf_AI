import tkinter as tk
from tkinter import *

def DetectAnimalsInRange(main_animal, other_animals) -> list:
    """Detect animals in range of the given animal, returns list of animals in range coords (x,y) """

    main_animal_coord_X, main_animal_coord_Y = main_animal.animal_location
    animals_in_range = []

    for other_animal in other_animals:
        other_animal_coord_X, other_animal_coord_Y = other_animal.animal_location

        if main_animal_coord_X in range(int(other_animal_coord_X - main_animal.animal_sight_range),int(other_animal_coord_X + main_animal.animal_sight_range)) and main_animal_coord_Y in range(int(other_animal_coord_Y - main_animal.animal_sight_range), int(other_animal_coord_Y + main_animal.animal_sight_range)):
            animals_in_range.append(other_animal.animal_location)
    
    return animals_in_range

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

def CheckForCollisions(best_move: tuple, main_animal: object, animals: list,board_rows_and_columns: tuple) -> bool:
    """Called to check if next animal move will result in collision """

    best_x, best_y = best_move
    current_wolf_x, current_wolf_y = main_animal.animal_location
    possible_new_x = current_wolf_x + best_x
    possible_new_y = current_wolf_y + best_y

    if CheckForAnimalCollision(main_animal,animals,possible_new_x,possible_new_y) and CheckForWallCollision(main_animal,possible_new_x,possible_new_y,board_rows_and_columns) == True:
        return True


def CheckForAnimalCollision(main_animal: object,animals: list[object],possible_new_x: int ,possible_new_y: int) -> bool:
    """Check if next move will collide with another animal """
    for animal in animals:
        if animal.animal_moving_to == (possible_new_x,possible_new_y) and animal.animal_ID != main_animal.animal_ID:
            return False
    return True


def CheckForWallCollision(main_animal: object, possible_new_x: int ,possible_new_y: int, board_rows_and_columns: tuple ) -> bool: 
    """Check if next move will collide with a wall """

    number_of_rows, number_of_columns = board_rows_and_columns

    if possible_new_x < 0 or possible_new_y < 0:
        return False
    if possible_new_x > number_of_rows or possible_new_y > number_of_columns:
        return False

    return True
