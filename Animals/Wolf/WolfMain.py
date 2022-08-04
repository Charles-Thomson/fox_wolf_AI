from Animals.SharedFunctunality import HelperFunctions
from Animals.SharedFunctunality import CollisionDetection




def MainWolfAI(wolfs: list[object], foxs: list[object],canvas_data: object) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for wolf in wolfs: 
        
        wolf.animal_move_data.animals_in_range = HelperFunctions.DetectAnimalsInRange(wolf,foxs)
        
        wolf.animal_movement_algorithm(wolf,collision_detection,canvas_data)
        HelperFunctions.SetAnimalMovingTo(wolf)
        HelperFunctions.MoveAnimal(wolf,canvas_data)
        HelperFunctions.UpdateAnimalData(wolf)
    
        
    