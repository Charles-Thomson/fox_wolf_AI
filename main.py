import NewSetUp as setup
from AI import NewFoxAI
from AI import NewWolfAI
import tkinter as tk


class main():
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.canvas_data, self.foxs, self.wolfs = setup.main(self.node_size,self.board_height,self.board_width)
        self.testNewFoxAI()
        self.testNewWolfAI()

    def testNewFoxAI(self):
        NewFoxAI.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)

    def testNewWolfAI(self):
        NewWolfAI.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)
    


        #  Do next:  
        # Re name methods to something mre applicable 
        # Collision detection in place
        # Refactor to use a loop instead of tail recursion in the supporting method 
        #
        # Clean up the supporting methods file !
        #

        # start looking at reverse A* 


if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 