import time
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
        #self.testNewFoxAI()
        #self.testNewWolfAI()
        self.run()
        
    def testNewFoxAI(self):
        NewFoxAI.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)

    def testNewWolfAI(self):
        NewWolfAI.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)

    def run(self) -> None:
        NewFoxAI.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)
        NewWolfAI.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)
        
        

        self.canvas_data.canvas.after(5000,self.run)


        #  Do next:  
        # Still have bugs in A*
        # Targeting is not working with prey higher to the left
        # Some times make very odd jumps on start ?
        # May need to move each path finding to new module as its messy af
        # A* looks like a freking mess currently

        # Issue to in DetermineBestMove again, need to clean up


if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 