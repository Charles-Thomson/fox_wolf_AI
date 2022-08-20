from HelperFunctions import HelperFunctions
from CollisionDetection import CollisionDetection
from Animals.NewAnimalDataClass import Animal
from GUI.Board import CanvasData


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
        HelperFunctions.CheckPreyAlive(foxs, wolfs, canvas_data)
        HelperFunctions.IncrementPreyScore(fox)
        HelperFunctions.UpdateAnimalData(fox)
