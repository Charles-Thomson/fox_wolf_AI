
import SetUp as setup
from Animals.Fox import FoxMain
from Animals.Wolf import WolfMain

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
        FoxMain.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)

    def testNewWolfAI(self):
        WolfMain.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)

    def run(self) -> None:
        FoxMain.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)
        WolfMain.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)
        
        self.canvas_data.canvas.after(1000,self.run)

        #  Do next:  
        #  Fix the need to pass the move i.e(1,-1) , out of the algorithms or implement a helper function to handle it - lots of dupe code currently
        # need to make bloacking 
        


if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 