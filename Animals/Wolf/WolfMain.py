from Animals.SharedFunctionality import HelperFunctions
from Animals.SharedFunctionality import CollisionDetection
from Animals.SharedFunctionality.NewAnimalDataClass import Animal
from Board import CanvasData


def MainWolfAI(
    wolfs: list[Animal], foxs: list[Animal], canvas_data: CanvasData
) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for wolf in wolfs:

        wolf.move_data.animals_in_range = HelperFunctions.DetectAnimalsInRange(
            wolf, foxs
        )

        wolf.animal_movement_algorithm(wolf, collision_detection, canvas_data)
        HelperFunctions.SetAnimalMovingTo(wolf)
        HelperFunctions.MoveAnimal(wolf, canvas_data)
        HelperFunctions.UpdateAnimalData(wolf)
