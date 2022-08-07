from Animals.SharedFunctionality import HelperFunctions
from Animals.SharedFunctionality import CollisionDetection
from Animals.SharedFunctionality.NewAnimalDataClass import Animal
from Board import CanvasData


def MainFoxAI(foxs: list[Animal], wolfs: list[Animal], canvas_data: CanvasData) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for fox in foxs:
        fox.move_data.animals_in_range = HelperFunctions.DetectAnimalsInRange(
            fox, wolfs
        )
        fox.animal_movement_algorithm(fox, collision_detection, canvas_data)
        print(fox)
        HelperFunctions.SetAnimalMovingTo(fox)
        HelperFunctions.MoveAnimal(fox, canvas_data)
        FoxAlive(fox, foxs, wolfs, canvas_data)
        HelperFunctions.UpdateAnimalData(fox)


# Needs refactoring
def FoxAlive(
    fox: Animal, foxs: list[Animal], wolfs: list[Animal], canvas_data: CanvasData
) -> None:
    """Check if the fox has been eatten"""

    for fox in foxs:
        for wolf in wolfs:
            if wolf.move_data.animal_location == fox.move_data.animal_location:
                print("Fox dead")
                foxs.remove(fox)
                canvas_data.canvas.delete(fox.core_data.animal_ID)
