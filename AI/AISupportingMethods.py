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
