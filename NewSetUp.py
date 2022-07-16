import tkinter as tk
from tkinter import Canvas
from AI import AISupportingMethods
import NewAnimalDataClass
import NewBoard

def main(node_size: int,canvas_height: int ,canvas_width: int) -> Canvas:
    """Setup - Create the board and generate animals"""

    CanvasData = NewBoard.BuildCanvas(canvas_height, canvas_width,node_size)
    foxs = GenerateFoxs()
    wolfs = GenerateWolfs()    
    DrawAnimalsOnCanvas(CanvasData.canvas, foxs)
    DrawAnimalsOnCanvas(CanvasData.canvas, wolfs)

    return CanvasData, foxs , wolfs
    
def GenerateFoxs() -> list:
    """Generate each fox and return as list"""
    
    fox_A = NewAnimalDataClass.SpawnAnimal(animal_type = NewAnimalDataClass.AnimalType.FOX,   
                                        animal_location = (5,5), 
                                        animal_sight_range = 4, 
                                        animal_draw_colour = "blue")

    return [fox_A]

def GenerateWolfs() -> list:
    """Generate each wolf and return as list"""

    wolf_A = NewAnimalDataClass.SpawnAnimal(animal_type= NewAnimalDataClass.AnimalType.WOLF, 
                                         animal_location=(7,7),
                                         animal_sight_range=4,
                                         animal_draw_colour = "red")
    return [wolf_A]


def DrawAnimalsOnCanvas(built_canvas: Canvas, animals: list[object]) -> None:
    """Draw animals to canvas - set the animal_ID and animal_move_data"""

    for animal in animals:
        coord_x, coord_y = animal.animal_core_data.animal_spawn_location
        x1,y1,x2,y2 = AISupportingMethods.ConvertToLongCoords(coord_x, coord_y, node_size = 20)

        # Change to a set animal data method 
        animal.animal_ID = built_canvas.create_rectangle(x1,y1,x2,y2, fill=animal.animal_core_data.animal_draw_colour)
        animal.animal_move_data.animal_location = animal.animal_core_data.animal_spawn_location



