import setup as st
import NewSetUp as setup
import time
from AI import fox_AI as fox_AI 
from AI import wolf_AI as wolf_AI
import foxAI as foxAI
import wolfAI as wolfAI

import tkinter as tk
from tkinter import *


class main():
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.built_canvas, self.foxs, self.wolfs = setup.main(parent,self.node_size,self.board_height,self.board_width)
        self.run_game()
    
    # change to run game ? - this will be the main loop 
    def run_game(self):
        foxAI.MainFoxAI(self.foxs,self.wolfs,self.built_canvas,self.node_size )
        wolfAI.MainWolfAI(self.wolfs,self.foxs, self.built_canvas, self.node_size)

        self.built_canvas.after(5000, self.run_game)

        # Do next  
        #  Implement collision for both animals types -> working through this issue currently 
        # Add to the data type of next full ocation , then can check if any location to be clashes 
        #  Detect thod iving all animals not just the opersit - only take in the type maybe to remove seperate wolf and fox list ?
        # -- this may come as a priority system later
        # need collision checking on the moves <- next step
        # currently working in new foxAI
        # 
        # 
        #look at logging instead of print /?



       

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 