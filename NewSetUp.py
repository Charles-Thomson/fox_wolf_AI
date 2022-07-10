import tkinter as tk
from tkinter import *
import AnimalDataClass
from AI import AISupportingMethods

import board

def main(node_size: int,board_height: int ,board_width: int) -> Canvas:
    built_canvas = build_canvas(node_size,board_height,board_width)
    foxs = GenerateFoxs()
    wolfs = GenerateWolfs()
    
    DrawAnimalsOnCanvas(built_canvas, foxs)
    DrawAnimalsOnCanvas(built_canvas, wolfs)

    return built_canvas, foxs , wolfs

def build_canvas(node_size,board_height,board_width) -> Canvas:
    board_canvas = board.board(node_size,board_height, board_width)
    built_canvas = board_canvas.BuildCanvas(board_height,board_width,node_size)
    return built_canvas

def GenerateFoxs() -> list:
    
    fox_A = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.FOX, 
                                         animal_location=(7,7),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")

    fox_B = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.FOX, 
                                         animal_location=(9,7),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")

    fox_C = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.FOX, 
                                         animal_location=(11,7),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")

    fox_D = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.FOX, 
                                         animal_location=(7,14),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")

    fox_E = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.FOX, 
                                         animal_location=(11,14),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")
    return [fox_A]

def GenerateWolfs() -> list:

    wolf_A = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(5,5),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_B = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(9,5),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_C = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(9,9),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_D = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(12,6),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_E = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(9,9),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_F = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(14,4),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_G = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(14,14),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_H = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(10,10),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_I = AnimalDataClass.SpawnNewAnimal(animal_type= AnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(4,16),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")
    return [wolf_A,wolf_B]


def DrawAnimalsOnCanvas(built_canvas, animals) -> None:
    for animal in animals:
        coord_x, coord_y = animal.animal_location
        x1,y1,x2,y2 = AISupportingMethods.ConvertToLongCoords(coord_x, coord_y,node_size = 20)
        animal.animal_ID = built_canvas.create_rectangle(x1,y1,x2,y2, fill=animal.animaml_draw_colour)
    



if __name__ == "__main__":
    root = tk.Tk()
    board = main(root)
    root.mainloop()
