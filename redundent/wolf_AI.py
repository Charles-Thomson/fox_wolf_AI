import tkinter as tk
from tkinter import *

from . import AISupportingMethods

class wolf_AI():
    def __init__(self, board_canvas,alive_wolf_locations, alive_fox_locations,node_size):
        self.built_canvas = board_canvas
        self.alive_wolf_locations = alive_wolf_locations
        self.alive_fox_locations = alive_fox_locations 
        self.node_size = node_size
        self.next_moves = []

    def detect_foxs_in_range_of_wolf(self):
        fox = self.alive_fox_locations[0]
        wolfs_with_fox_in_range = set()
        for wolf in self.alive_wolf_locations:
            foxs_in_range = AISupportingMethods.detect_animals_in_range(wolf,self.alive_fox_locations,self.built_canvas, self.node_size, sight_range = 4)
            if foxs_in_range: wolfs_with_fox_in_range.add(wolf)

        self.determine_best_move(wolfs_with_fox_in_range,fox)

    
    def move_wolf(self,wolf,new_wolf_coord_x,new_wolf_coord_y):
        #print("moving wolf - {wolf}")
        self.built_canvas.move(wolf,new_wolf_coord_x,new_wolf_coord_y)
        print("moveing wolf by",new_wolf_coord_x,new_wolf_coord_y)

    def collision_check(self, coord_x, coord_y) -> bool:
        if (coord_x, coord_y) not in self.next_moves:
            return True

    # Basic functunality currently
    def determine_best_move(self, wolfs_with_fox_in_range, fox):
        fox_coord_x, fox_coord_y = AISupportingMethods.convert_to_short_coords(fox,self.built_canvas,self.node_size)
       
        for wolf in wolfs_with_fox_in_range:
            wolf_coord_x, wolf_coord_y = AISupportingMethods.convert_to_short_coords(wolf,self.built_canvas, self.node_size)
            
            new_wolf_coord_x = 0
            new_wolf_coord_y = 0

            if fox_coord_x > wolf_coord_x:
                new_wolf_coord_x = 20
            
            if fox_coord_y > wolf_coord_y:
                new_wolf_coord_y = 20

            if fox_coord_x < wolf_coord_x:
                new_wolf_coord_x = -20
            
            if fox_coord_y < wolf_coord_y:
                new_wolf_coord_y = -20
            
            if self.collision_check(new_wolf_coord_x,new_wolf_coord_y):
                print(f"{wolf} allowed to move")
                self.next_moves.append((new_wolf_coord_x,new_wolf_coord_y))
                self.move_wolf(wolf,new_wolf_coord_x,new_wolf_coord_y)





        