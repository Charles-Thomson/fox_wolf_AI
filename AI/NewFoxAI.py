import tkinter as tk
from AI import AISupportingMethods
import collections
from tkinter import Canvas

# this works
def MainFoxAI(foxs: list, wolfs: list):
    for fox in foxs:
        fox.animal_move_data.animals_in_range = AISupportingMethods.DetectAnimalsInRange(fox,wolfs)
        fox.animal_movement_algorithm(fox)
        print(fox)






