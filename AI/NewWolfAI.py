import tkinter as tk
from AI import AISupportingMethods
from AI import CollisionDetection
from tkinter import Canvas


def MainWolfAI(wolfs: list[object], foxs: list[object],canvas_data: object) -> None:
    collision_detection = CollisionDetection.CollisionDetection(canvas_data)
    for wolf in wolfs: 
        wolf.animal_move_data.animals_in_range = AISupportingMethods.DetectAnimalsInRange(wolf,foxs)
        wolf.animal_movement_algorithm(wolf,collision_detection,canvas_data)
        AISupportingMethods.SetAnimalMovingTo(wolf)
        AISupportingMethods.MoveAnimal(wolf,canvas_data)
        print(wolf)
        AISupportingMethods.UpdateAnimalData(wolf)
    
        
    