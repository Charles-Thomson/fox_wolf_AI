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
        self.board_rows_and_columns = self.GetRowsAndColumns()
        self.built_canvas, self.foxs, self.wolfs = setup.main(self.node_size,self.board_height,self.board_width)
        #self.fox_thread = threading.Thread(target=self.RunFoxs)
        #self.wolf_thread = threading.Thread(target=self.RunWolfs)
        self.RunGame()
    
    def RunGame(self) -> None:
        """Run the main wof and fox threads"""

        foxAI.MainFoxAI(self.foxs,self.wolfs, self.built_canvas, self.node_size, self.board_rows_and_columns)
        wolfAI.MainWolfAI(self.wolfs,self.foxs, self.built_canvas, self.node_size,self.board_rows_and_columns)
        # Checking for death in here
        self.IsFoxDead()
        self.built_canvas.after(2000, self.RunGame)

        # Not threading for testing 
        #self.fox_thread.start()
        #self.wolf_thread.start()

    # Moved both into threads - Testing 

    def RunFoxs(self) -> None:
        """Run the fox in threading"""

        foxAI.MainFoxAI(self.foxs,self.wolfs, self.built_canvas, self.node_size, self.board_rows_and_columns)
        self.IsFoxDead()
        self.built_canvas.after(2000, self.RunFoxs)

    def RunWolfs(self) -> None:
        """Run the wolf in with threading"""

        wolfAI.MainWolfAI(self.wolfs,self.foxs, self.built_canvas, self.node_size,self.board_rows_and_columns)
        self.built_canvas.after(3000, self.RunWolfs)

    # Only in here until i find a beter place
    def GetRowsAndColumns(self) -> tuple:
        """Get the number of rows and columns on the canvas """

        number_of_rows = int(self.board_width / self.node_size)
        number_of_columns = int(self.board_width / self.node_size)
        return (number_of_rows - 1, number_of_columns - 1 )

    def IsFoxDead(self) -> None: 
        """Check if a fox is dead -> if dead remove from list and delte from canvas"""

        for fox in self.foxs:
            if any(fox.animal_location == wolf.animal_location for wolf in self.wolfs):
                self.foxs.remove(fox)
                self.built_canvas.delete(fox.animal_ID)
                print("A Fox is dead")


        #  Do next:  
        # Fox and Wolf data classes refactored - now using protocol - need to refactor rest of project to accomodate

        #  Fox movment needs to be improved
        #  - Move over to a better way to detect and move 
        #  - issue with finding the best move and carrying in out <- possibalycollision checking issue
        #  
        #  Issues: 
        #  Collision is currently quite clunky - find a better way 
        #  Fox move has bug -> more moves can be made but freezes in place
        # 
        # 
        #look at logging instead of print /?



       

        # start looking at reverse A* 


        



if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 