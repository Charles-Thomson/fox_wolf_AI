import tkinter as tk
from tkinter import *

from AI import AI_supporting_methods

class wolf_AI():
    def __init__(self, board_canvas,alive_wolf_locations, alive_fox_locations,node_size):
        self.built_canvas = board_canvas
        self.alive_wolf_locations = alive_wolf_locations
        self.alive_fox_locations = alive_fox_locations 
        self.node_size = node_size

    def detect_foxs_in_range_of_wolf(self):
        fox = self.alive_fox_locations[0]
        wolfs_with_fox_in_range = set()
        wolfs_with_fox_in_range = AI_supporting_methods.detect_animals_in_range(fox,self.alive_wolf_locations,self.built_canvas, self.node_size)

        #print("Wolfs with a fox in range", wolfs_with_fox_in_range)

        self.determine_best_move(wolfs_with_fox_in_range,fox)

    
    def move_wolf(self,wolf,new_wolf_coord_x,new_wolf_coord_y):
        #print("moving wolf - {wolf}")
        self.built_canvas.move(wolf,new_wolf_coord_x,new_wolf_coord_y)
        print("moveing wolf by",new_wolf_coord_x,new_wolf_coord_y)

    # Basic functunality currently
    def determine_best_move(self, wolfs_with_fox_in_range, fox):
        fox_coord_x, fox_coord_y = AI_supporting_methods.convert_to_short_coords(fox,self.built_canvas,self.node_size)
       
        for wolf in wolfs_with_fox_in_range:
            wolf_coord_x, wolf_coord_y = AI_supporting_methods.convert_to_short_coords(wolf,self.built_canvas, self.node_size)
            
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
            
            self.move_wolf(wolf,new_wolf_coord_x,new_wolf_coord_y)




        