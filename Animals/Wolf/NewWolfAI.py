from Animals.SharedFunctunality import HelperFuntions
from Animals.SharedFunctunality import CollisionDetection

from Animals.Wolf.WolfMovmentAlgorithms import WolfMovementAlgorithms


def MainWolfAI(wolfs: list[object], foxs: list[object],canvas_data: object) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for wolf in wolfs: 
        
        wolf.animal_move_data.animals_in_range = HelperFuntions.DetectAnimalsInRange(wolf,foxs)
        
        wolf.animal_movement_algorithm(wolf,collision_detection,canvas_data)
        HelperFuntions.SetAnimalMovingTo(wolf)
        
        HelperFuntions.MoveAnimal(wolf,canvas_data)
        
        HelperFuntions.UpdateAnimalData(wolf)
    
        
    