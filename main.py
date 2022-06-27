import setup as st
import time
from AI import fox_AI as fox_AI 
from AI import wolf_AI as wolf_AI

import tkinter as tk
from tkinter import *


class main():
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
        
        fox_AI.detect_wolfs_in_range_of_fox(self.alive_fox_locations,self.alive_wolf_locations,self.built_canvas,self.node_size)
        wolf_AI_object = wolf_AI.wolf_AI(self.built_canvas,self.alive_wolf_locations,self.alive_fox_locations, self.node_size)
        wolf_AI_object.detect_foxs_in_range_of_wolf()
        #fox_AI.detect_wolfs_in_range_of_fox(self.alive_fox_locations,self.alive_wolf_locations,self.built_canvas,self.node_size)
        self.built_canvas.after(5000, self.start_game)




        # Do next  
        #         - rethink the fox move 
        #         - wolfs can now move 
        #         - put the fox and wolf elements into seperate threads 
        #         - Bug with fox movement still - might be time to redesign
        #         - need collision - sides and other animals
        #         - need finish (kill of fox)
        #

        #         - refactor detect method to use range - not hard coded - to allow for different sight ranges 



       

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 