import NewSetUp as setup
from AI import foxAI 
from AI import wolfAI
import tkinter as tk

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
        #self.RunGame()
    
    def RunGame(self) -> None:
        """Run the main wof and fox threads"""

        foxAI.MainFoxAI(self.foxs,self.wolfs, self.built_canvas, self.node_size, self.board_rows_and_columns)
        wolfAI.MainWolfAI(self.wolfs,self.foxs, self.built_canvas, self.node_size,self.board_rows_and_columns)


        # Checking for death in here
        self.IsFoxDead()
        self.built_canvas.after(2000, self.RunGame)

    def IsFoxDead(self) -> None: 
        """Check if a fox is dead -> if dead remove from list and delte from canvas"""

        for fox in self.foxs:
            if any(fox.animal_location == wolf.animal_location for wolf in self.wolfs):
                self.foxs.remove(fox)
                self.built_canvas.delete(fox.animal_ID)
                print("A Fox is dead")


        #  Do next:  
        # Refactoring - Board 
        # Then NewFoxAI
        # Then NewWolfAI 
        # -> inc te uspporting functions for both
        #
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

 