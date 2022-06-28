import tkinter as tk
from tkinter import *
import AnimalDataClass
import logging
from AI import AI_supporting_methods

import board

def main(root) -> Canvas:
    built_canvas = build_canvas(root,node_size = 20,board_height = 500 ,board_width = 500)
    foxs = GenerateFoxs()
    wolfs = GenerateWolfs()

    DrawAnimalsOnCanvas(built_canvas, foxs)


def build_canvas(parent,node_size,board_height,board_width) -> Canvas:
    board_canvas = board.board(parent,node_size,board_height, board_width)
    built_canvas = board_canvas.build_canvas(parent,board_height,board_width,node_size)
    return built_canvas

def GenerateFoxs() -> list:
    
    fox_A = AnimalDataClass.SpawnNewAnimal(animal_type= "Fox", 
                                         animal_location=(5,5),
                                         animal_sight_range=2)
    return [fox_A]

def GenerateWolfs() -> list:

    wolf_A = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(5,4),
                                         animal_sight_range=3)

    wolf_B = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(3,4),
                                         animal_sight_range=3)

    wolf_C = AnimalDataClass.SpawnNewAnimal(animal_type= "Wolf", 
                                         animal_location=(3,4),
                                         animal_sight_range=3)
    return [wolf_A,wolf_B,wolf_C]


def DrawAnimalsOnCanvas(built_canvas, animals) -> None:
    for animal in animals:
        x1,y1,x2,y2 = AI_supporting_methods.ConverToLongCoords(animal.animal_location,node_size = 20)
        #print(x1,y1,x2,y2)
        logging.debug(x1,y1,x2,y2)




if __name__ == "__main__":
    root = tk.Tk()
    board = main(root)
    root.mainloop()
