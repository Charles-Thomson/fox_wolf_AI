import setup as st
import NewSetUp as setup
import time
from AI import fox_AI as fox_AI 
from AI import wolf_AI as wolf_AI
import foxAI as foxAI
import wolfAI as wolfAI

import tkinter as tk
from tkinter import *

import threading 


class main():
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.built_canvas, self.foxs, self.wolfs = setup.main(parent,self.node_size,self.board_height,self.board_width)
        self.fox_thread = threading.Thread(target=self.RunFoxs)
        self.wolf_thread = threading.Thread(target=self.RunWolfs)
        self.run_game()
    
    # change to run game ? - this will be the main loop 
    def run_game(self):
        self.fox_thread.start()
        self.wolf_thread.start()

    # Moved both into threads - Testing 
    def RunFoxs(self) -> None:
        foxAI.MainFoxAI(self.foxs,self.wolfs,self.built_canvas,self.node_size )
        self.built_canvas.after(2000, self.RunFoxs)

    def RunWolfs(self) -> None:
        wolfAI.MainWolfAI(self.wolfs,self.foxs, self.built_canvas, self.node_size)
        self.built_canvas.after(3000, self.RunWolfs)


        # Do next  
        #  Implement collision for both animals types -> very basic , only fox to fox
        #  Moved into threads - works 
        #  Add in fox death 
        #  Fox move/detect needs work as it locks up when more moves can be made
        # 
        # 
        # 
        # 
        #look at logging instead of print /?



       

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 