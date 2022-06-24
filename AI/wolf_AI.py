import tkinter as tk
from tkinter import *

class wolf_AI():
    def __init__(self, board_canvas,alive_wolf_locations, alive_fox_locations):
        self.built_canvas = board_canvas
        self.alive_wolf_locations = alive_wolf_locations
        self.alive_fox_locations = alive_fox_locations 

    def detect_foxs_in_range(self):
        fox = self.alive_fox_locations[0]
        foxs_in_range = set()

        fox_x1,fox_y1,fox_x2,fox_y2 = self.built_canvas.coords(fox)

        for wolf in self.alive_wolf_locations:
            wolf_x1,wolf_y1,wolf_x2,wolf_y2 = self.built_canvas.coords(wolf)

            if fox_x1 in range(int(wolf_x1 - 60), int(wolf_x1 + 60) and wolf_y1 in range(int(fox_y1 - 60), int(fox_y1 + 60))):
                foxs_in_range.add(fox)

            if fox_x2 in range(int(wolf_x2 - 60),int(wolf_x2 + 60)and fox_y2 in range(int(wolf_y2 - 60), int(wolf_y2 + 60))):
                foxs_in_range.add(fox)

        print("foxs in range of wolf", foxs_in_range)

        



    def determine_best_move(self,alive_wolf_locations,alive_fox_locations):
        print("null")