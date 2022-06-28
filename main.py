import setup as st
import NewSetUp as setup
import time
from AI import fox_AI as fox_AI 
from AI import wolf_AI as wolf_AI
import foxAI as foxAI

import tkinter as tk
from tkinter import *


class main():
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.built_canvas, self.foxs, self.wolfs = setup.main(parent,self.node_size,self.board_height,self.board_width)
        self.start_game()
    
    # change to run game ? - this will be the main loop 
    def start_game(self):
        foxAI.DetectWolfsInRange(self.foxs,self.wolfs,self.built_canvas,self.node_size)
        #fox_AI.detect_wolfs_in_range_of_fox(self.alive_fox_locations,self.alive_wolf_locations,self.built_canvas,self.node_size)
        #wolf_AI_object = wolf_AI.wolf_AI(self.built_canvas,self.alive_wolf_locations,self.alive_fox_locations, self.node_size)
        #wolf_AI_object.detect_foxs_in_range_of_wolf()

        #self.built_canvas.after(5000, self.start_game)




        # Do next  
        # continue with refactoring to use the dataclass approach
        # currently working in new foxAI
        # 
        # 
        #look at logging instead of print /?



       

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 