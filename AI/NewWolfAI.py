import tkinter as tk
from AI import AISupportingMethods
from tkinter import Canvas

def MainWolfAI(wolfs: list[object], foxs: list[object],canvas_data: object) -> None:
    for wolf in wolfs: 
        wolf.animal_move_data.animals_in_range = AISupportingMethods.DetectAnimalsInRange(wolf,foxs)
        wolf.animal_movement_algorithm(wolf)
        AISupportingMethods.SetAnimalMovingTo(wolf)
        print(wolf)