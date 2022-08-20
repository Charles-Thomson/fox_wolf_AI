from tkinter import Canvas
from HelperFunctions import HelperFunctions
import Animals.NewAnimalDataClass as NewAnimalDataClass
from Animals.NewAnimalDataClass import Animal
import GUI.Board as Board
from Setup import DataRead
from Setup.DataRead import AnimalSpawnData


def main(node_size: int, canvas_height: int, canvas_width: int) -> tuple:
    """Setup - Create the board and generate animals"""

    CanvasData = Board.BuildCanvas(canvas_height, canvas_width, node_size)
    foxs_spawn_data, wolfs_spawn_data = DataRead.ReadInData()

    foxs = GenerateFoxs(foxs_spawn_data)
    wolfs = GenerateWolfs(wolfs_spawn_data)

    DrawAnimalsOnCanvas(CanvasData.canvas, foxs)
    DrawAnimalsOnCanvas(CanvasData.canvas, wolfs)

    return CanvasData, foxs, wolfs


def GenerateFoxs(foxs_spawn_data: list[AnimalSpawnData]) -> list[Animal]:
    """Generate each fox and return as list"""

    foxs = []
    for element in foxs_spawn_data:
        new_fox = NewAnimalDataClass.SpawnAnimal(
            animal_type=NewAnimalDataClass.AnimalType.FOX,  # Keep as enum form
            animal_location=element["spawn_location"],
            animal_sight_range=element["sight_range"],
            animal_movement_algorithm=element["movement_algorithm"],
            animal_draw_colour="blue",
        )
        foxs.append(new_fox)
    return foxs


def GenerateWolfs(wolfs_spawn_data) -> list[Animal]:
    """Generate each wolf and return as list"""

    wolfs = []
    for element in wolfs_spawn_data:
        new_wolf = NewAnimalDataClass.SpawnAnimal(
            animal_type=NewAnimalDataClass.AnimalType.WOLF,
            animal_location=element["spawn_location"],
            animal_sight_range=element["sight_range"],
            animal_movement_algorithm=element["movement_algorithm"],
            animal_draw_colour="red",
        )
        wolfs.append(new_wolf)
    return wolfs


def DrawAnimalsOnCanvas(built_canvas: Canvas, animals: list[Animal]) -> None:
    """Draw animals to canvas - set the animal_ID and animal_move_data"""

    for animal in animals:
        coord_x, coord_y = animal.core_data.animal_spawn_location
        x1, y1, x2, y2 = HelperFunctions.ConvertToLongCoords(
            coord_x, coord_y, node_size=20
        )

        # Change to a set animal data method
        animal.core_data.animal_ID = built_canvas.create_rectangle(
            x1, y1, x2, y2, fill=animal.core_data.animal_draw_colour
        )
        animal.move_data.animal_location = animal.core_data.animal_spawn_location
