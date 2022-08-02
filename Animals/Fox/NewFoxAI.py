import tkinter as tk
from Animals.SharedFunctunality import HelperFuntions
from Animals.SharedFunctunality import CollisionDetection
import collections


# this works
def MainFoxAI(foxs: list[object], wolfs: list[object], canvas_data: object) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for fox in foxs:
        fox.animal_move_data.animals_in_range = HelperFuntions.DetectAnimalsInRange(fox,wolfs)
        fox.animal_movement_algorithm(fox,collision_detection)
        HelperFuntions.SetAnimalMovingTo(fox)
        HelperFuntions.MoveAnimal(fox,canvas_data)
        FoxAlive(fox,foxs,wolfs,canvas_data) 
        HelperFuntions.UpdateAnimalData(fox)
        

# Needs refactoring
def FoxAlive(fox: object,foxs: list[object], wolfs: list[object], canvas_data: object) -> bool: 
    """Check if the fox has been eatten"""

    for fox in foxs:
        for wolf in wolfs:
            if wolf.animal_move_data.animal_location == fox.animal_move_data.animal_location:
                print("Fox dead")
                foxs.remove(fox)
                canvas_data.canvas.delete(fox.animal_core_data.animal_ID)

        

    






