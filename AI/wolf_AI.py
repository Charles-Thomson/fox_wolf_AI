import tkinter as tk
from tkinter import *

from AI import AI_supporting_methods

class wolf_AI():
    def __init__(self, board_canvas,alive_wolf_locations, alive_fox_locations,node_size):
        self.built_canvas = board_canvas
        self.alive_wolf_locations = alive_wolf_locations
        self.alive_fox_locations = alive_fox_locations 
        self.node_size = node_size

    def detect_wolfs_in_range_of_fox(self):
        fox = self.alive_fox_locations[0]
        foxs_in_range = set()
        wolfs_in_range_of_fox = AI_supporting_methods.detect_animals_in_range(fox,self.wolf_alive_locations,self.built_canvas, self.node_size)

        print("foxs in range of wolf", wolfs_in_range_of_fox)

        



    def determine_best_move(self,alive_wolf_locations,alive_fox_locations):
        print("null")