import tkinter as tk
from tkinter import *

def detect_animals_in_range(main_animal, other_animals, built_canvas, node_size, sight_range) -> list:
    main_animal_coords = convert_to_short_coords(main_animal, built_canvas,node_size)
    main_animal_coord_x = main_animal_coords[0]
    main_animal_coord_y = main_animal_coords[1]
    animals_in_range = set()
    
    for other_animal in other_animals:
        other_animal_coords = convert_to_short_coords(other_animal, built_canvas,node_size)
        other_animal_coord_x = other_animal_coords[0]
        other_animal_coord_y = other_animal_coords[1]

        if main_animal_coord_x in range(int(other_animal_coord_x - sight_range), int(other_animal_coord_x + sight_range)) and main_animal_coord_y in range(int(other_animal_coord_y - sight_range), int(other_animal_coord_y + sight_range)):
                animals_in_range.add(other_animal)

    return animals_in_range


def convert_to_short_coords(animal,built_canvas, node_size):
    x1,y1,x2,y2 = built_canvas.coords(animal)
    x = (x1 / node_size)
    y = (y1 / node_size)

    return (x,y) 

def ConverToLongCoords(animal_location,node_size) -> int:
    animal_x, animal_y = animal_location
    x1 = (animal_x * node_size)
    y1 = (animal_y * node_size)
    x2 = x1 + node_size
    y2 = y1 + node_size

    return x1,y1,x2,y2
