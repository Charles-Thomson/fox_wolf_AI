from tkinter import Canvas
from Animals.SharedFunctionality import HelperFunctions
import Animals.SharedFunctionality.NewAnimalDataClass as NewAnimalDataClass
import Board
from Animals.SharedFunctionality.NewAnimalDataClass import Animal


def main(node_size: int, canvas_height: int, canvas_width: int) -> tuple:
    """Setup - Create the board and generate animals"""

    CanvasData = Board.BuildCanvas(canvas_height, canvas_width, node_size)
    foxs = GenerateFoxs()
    wolfs = GenerateWolfs()
    DrawAnimalsOnCanvas(CanvasData.canvas, foxs)
    DrawAnimalsOnCanvas(CanvasData.canvas, wolfs)

    return CanvasData, foxs, wolfs


def GenerateFoxs() -> list:
    """Generate each fox and return as list"""

    fox_A = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.FOX,
        animal_location=(4, 4),
        animal_sight_range=4,
        animal_draw_colour="blue",
    )

    fox_B = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.FOX,
        animal_location=(13, 13),
        animal_sight_range=4,
        animal_draw_colour="blue",
    )

    return [fox_A, fox_B]


def GenerateWolfs() -> list:
    """Generate each wolf and return as list"""

    wolf_A = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.WOLF,
        animal_location=(16, 16),
        animal_sight_range=4,
        animal_draw_colour="red",
    )

    wolf_B = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.WOLF,
        animal_location=(2, 2),
        animal_sight_range=4,
        animal_draw_colour="red",
    )

    wolf_C = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.WOLF,
        animal_location=(16, 7),
        animal_sight_range=4,
        animal_draw_colour="red",
    )

    wolf_D = NewAnimalDataClass.SpawnAnimal(
        animal_type=NewAnimalDataClass.AnimalType.WOLF,
        animal_location=(12, 12),
        animal_sight_range=4,
        animal_draw_colour="red",
    )
    return [wolf_A, wolf_B, wolf_C, wolf_D]


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


# Not yet being used
# def AnimalGeneration(
# number_of_foxs, number_of_wolfs, canvas_data
# ) -> list[object]:
#    """Gernates animals at random locations on the canvas"""
#
#  board_restriction_rows = canvas_data.number_of_rows
#    board_restriction_columns = canvas_data.number_of_columns
#    foxs = []
#    wolfs = []
#
#    for fox in range(0, number_of_foxs):
#        fox = NewAnimalDataClass.SpawnAnimal(
#            animal_type=NewAnimalDataClass.AnimalType.FOX,
#            animal_location=(
#                randrange(board_restriction_rows),
#                randrange(board_restriction_columns),
#            ),
#            animal_sight_range=4,
#            animal_draw_colour="blue",
#        )
#        foxs.append(fox)
#
#    for wolf in range(0, number_of_wolfs):
#        wolf = NewAnimalDataClass.SpawnAnimal(
#            animal_type=NewAnimalDataClass.AnimalType.WOLF,
#            animal_location=(
#                randrange(board_restriction_rows),
#                randrange(board_restriction_columns),
#            ),
#            animal_sight_range=4,
#            animal_draw_colour="blue",
#        )
#        wolfs.append(wolf)
#
#    return foxs, wolfs
