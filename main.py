
import setup as st
from AI import fox_AI as fox_AI 
from AI import wolf_AI as wolf_AI

import tkinter as tk
from tkinter import *
root = Tk()

class main(tk.Frame):
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.alive_fox_locations, self.alive_wolf_locations, self.built_canvas = self.start_setup(parent,node_size,board_height,board_width)
        # One fox support currently 
        self.fox = self.alive_fox_locations[0]
        self.start_game()

        #self.test_move_method()
    def start_setup(self,parent,node_size,board_height,board_width):
        alive_fox_locations, alive_wolf_locations, built_canvas = st.set_up(parent,node_size,board_height,board_width)
        return alive_fox_locations, alive_wolf_locations, built_canvas
    
    # change to run game ? - this will be the main loop 
    def start_game(self):
        #wolf_AI_object = wolf_AI.wolf_AI(self.built_canvas,self.alive_wolf_locations,self.alive_fox_locations)
        #wolf_AI_object.detect_foxs_in_range()
        fox_AI.detect_wolfs_in_range(self.alive_fox_locations,self.alive_wolf_locations,self.built_canvas,self.node_size)
        #self.built_canvas.after(5000, self.start_game )




        # Do next 
        #         - refactoring detect method into own file along with short_coords 
        #         - detect method now using short coords 
        #         - Next: Wolf movement towards the fox



        # fox_sight_range_detection - woring from the two points , may change to short coords to make better 

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 