import tkinter as tk
from tkinter import *
import AnimalDataClass
import logging
from AI import AISupportingMethods

import board

def main(root,node_size,board_height,board_width) -> Canvas:
    built_canvas = build_canvas(root,node_size,board_height,board_width)
    foxs = GenerateFoxs()
    wolfs = GenerateWolfs()
    

    DrawAnimalsOnCanvas(built_canvas, foxs)
    DrawAnimalsOnCanvas(built_canvas, wolfs)

    return built_canvas, foxs , wolfs


def build_canvas(parent,node_size,board_height,board_width) -> Canvas:
    board_canvas = board.board(parent,node_size,board_height, board_width)
    built_canvas = board_canvas.build_canvas(parent,board_height,board_width,node_size)
    return built_canvas

def GenerateFoxs() -> list:
    
    fox_A = AnimalDataClass.SpawnNewAnimal(animal_type= "Fox", 
                                         animal_location=(3,6),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")

    fox_B = AnimalDataClass.SpawnNewAnimal(animal_type= "Fox", 
                                         animal_location=(4,3),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "blue")
    return [fox_A]

def GenerateWolfs() -> list:

    wolf_A = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(5,5),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_B = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(3,15),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")

    wolf_C = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(1,5),
                                         animal_sight_range=4,
                                         animaml_draw_colour = "red")
    return [wolf_A,wolf_B,wolf_C]


def DrawAnimalsOnCanvas(built_canvas, animals) -> None:
    for animal in animals:
        coord_x, coord_y = animal.animal_location
        x1,y1,x2,y2 = AISupportingMethods.ConvertToLongCoords(coord_x, coord_y,node_size = 20)
        animal.animal_ID = built_canvas.create_rectangle(x1,y1,x2,y2, fill=animal.animaml_draw_colour)
    



if __name__ == "__main__":
    root = tk.Tk()
    board = main(root)
    root.mainloop()
