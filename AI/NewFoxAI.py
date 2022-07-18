import tkinter as tk
from AI import AISupportingMethods
from AI import CollisionDetection
import collections


# this works
def MainFoxAI(foxs: list[object], wolfs: list[object], canvas_data: object) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for fox in foxs:
        fox.animal_move_data.animals_in_range = AISupportingMethods.DetectAnimalsInRange(fox,wolfs)
        fox.animal_movement_algorithm(fox,collision_detection)
        AISupportingMethods.SetAnimalMovingTo(fox)
        print(fox)

        # now need move 
        # now need update data






